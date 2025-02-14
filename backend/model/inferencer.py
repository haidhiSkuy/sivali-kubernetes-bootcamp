import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
import onnxruntime as ort 


class AlzheimerPredictor:
    def __init__(self):
        self.session = ort.InferenceSession("model/alzheimer_predictor.onnx")
        self.input_name = self.session.get_inputs()[0].name
        self.labels = {
            0:'Mild Demented', 1:'Moderate Demented', 
            2:'Non Demented', 3:'Very Mild Demented'
        }

    def base64_to_numpy(self, base64_str):
        image_bytes = base64.b64decode(base64_str)
        image = Image.open(BytesIO(image_bytes))
        img_array = np.array(image)
        return img_array
    
    def softmax(self, x):
        exp_values = np.exp(x - np.max(x))  # Stabilitas numerik (menghindari overflow)
        return exp_values / np.sum(exp_values)

    def preprocessing(self, base64_str): 
        image_array = self.base64_to_numpy(base64_str)
        image_array = cv2.resize(image_array, (200,200)) / 255.0 
        image_array = np.transpose(image_array, axes=(2,0,1)) 
        image_array = np.expand_dims(image_array, axis=0) 
        return image_array.astype(np.float32)

    def predict(self, base64_image): 
        preprocessed = self.preprocessing(base64_image) 
        outputs = self.session.run(None, {self.input_name: preprocessed})[0][0]
        outputs = self.softmax(outputs)
        prediction = np.argmax(outputs) 
        return self.labels[prediction]
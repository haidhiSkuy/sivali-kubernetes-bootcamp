import os
import requests 


class SendRequest: 
    def __init__(self):
        self.endpoint = os.getenv("ML_ENDPOINT")
        self.headers = headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def send_predict_request(self, input_image_base64 : str, patient_name : str):
        json_data = {
            'input_image_base64': input_image_base64,
            'patient_name': patient_name,
        }
        print(f"ENDPOINT : {self.endpoint}")
        response = requests.post(self.endpoint, headers=self.headers, json=json_data)
        return response.json()
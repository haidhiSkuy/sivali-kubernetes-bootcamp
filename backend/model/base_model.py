from pydantic import BaseModel 

class InputModel(BaseModel): 
    input_image_base64 : str 
    patient_name : str
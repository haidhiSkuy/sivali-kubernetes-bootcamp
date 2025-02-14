from fastapi import FastAPI
from model.base_model import InputModel
from model.inferencer import AlzheimerPredictor
from db.insert_prediction import PostgresDb
from dotenv import load_dotenv
load_dotenv()

db = PostgresDb()
predictor = AlzheimerPredictor()
app = FastAPI()

@app.post("/predict")
async def predict(input_model : InputModel):
    base64_image = input_model.input_image_base64 
    patient_name = input_model.patient_name
    prediction = predictor.predict(base64_image) 
    db.insert(patient_name, prediction)

    return {"prediction" : prediction}


if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=4444, log_level="info", reload=False)
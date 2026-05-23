from fastapi import FastAPI
from bmi_calculator import bmi_calculator

app = FastAPI()

@app.get("/bmi")
def get_bmi(weight:float,height:float):
    bmi,cat = bmi_calculator(height,weight)
    return {'BMI':round(bmi,2),
            'category':cat}
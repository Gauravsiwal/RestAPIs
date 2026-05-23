from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to home page"

@app.get("/info")
def info():
    return {'message':'This page is created by Gaurav Siwal'}

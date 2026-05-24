from fastapi import APIRouter
from model import Student
from logic import show_students, add_student

routes = APIRouter()

@routes.get('/student')
def fetch_students():
    return {"students": show_students()}

@routes.post('/student')
def create_student(student:Student):
    return add_student(student)
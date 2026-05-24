students = []

def show_students():
    return students

def add_student(data):
    students.append(data.dict())
    return {"message":"Student added Successfully",
            "Data":data}

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Student Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Student", "View Students"]
)

# ADD STUDENT
if menu == "Add Student":

    st.header("Add New Student")

    name = st.text_input("Enter Name")
    course = st.text_input("Enter Course")
    age = st.number_input("Enter Age", min_value=1)

    if st.button("Add Student"):

        student_data = {
            "name": name,
            "course": course,
            "age": age
        }

        response = requests.post(
            f"{BASE_URL}/student",
            json=student_data
        )

        if response.status_code == 200:
            st.success("Student added successfully!")
            st.json(response.json())

        else:
            st.error("Failed to add student")


# VIEW STUDENTS
elif menu == "View Students":

    st.header("All Students")

    response = requests.get(f"{BASE_URL}/student")

    if response.status_code == 200:

        students = response.json()

        st.json(students)

    else:
        st.error("Failed to fetch students")
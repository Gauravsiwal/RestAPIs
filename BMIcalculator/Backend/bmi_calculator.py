def bmi_calculator(height,weight):
    height = height/100 # cms to m
    bmi = weight/(height**2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi,category
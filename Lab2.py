print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    BMI=weight/(height * height)

    print("BMI = "+str(BMI))
    
    if BMI<18.5:
        print("Under Weight")
    elif 18.5<=BMI<=25.0:
        print("Normal Weight")
    else:
        print("Over Weight")
calculate_bmi(weight=57, height=1.70)
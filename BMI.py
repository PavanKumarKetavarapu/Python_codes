bmi=int(input("please enter 1 for  method-1 computation or enter 2 for method-2 computation: "))
if bmi==1:
    h=float(input("enter the height of the body in inches: "))
    w=float(input("enter the weight of the body in pounds: "))
    BMI=(w/(h*h))*703
    print("BMI of the body is",BMI)
elif bmi==2:
    h = float(input("enter the height of the body in meters: "))
    w = float(input("enter the weight of the body in kilograms: "))
    BMI=w/(h*h)
    print("BMI of the body is", BMI)
else:
    print("invalid input,please re-enter the correct input")
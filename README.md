# health_calc
weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in meters:"))

bmi=weight/(height**2)

print(f"Your BMI is:",bmi)

if bmi<18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Status: Normal weight")
else:
    print("Status: Over weight")
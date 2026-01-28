weight=float(input("enter your weight in kg:"))
height_feet=float(input("enter your height in feet(e.g.,5):"))
height_inches=float(input("enter remaining inches(e.g.,6):"))
#calculation
total_inches=(height_feet*12)+height_inches
height_meters=total_inches*0.0254
#BMI calculate
bmi=weight/(height_meters**2)

print(f"your BMI is:{bmi:.2f}" )

if bmi < 18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Status: Normal weight")
else:
    print("Status: Overweight")
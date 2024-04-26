height=float(input("Zadaj tvoju vysku (cm): "))
weight=float(input("Zadaj tvoju hmotnost (kg): "))

bmi=weight / (height/100)**2

if bmi <= 18.5:
    print(bmi)
    print("Underweight")
elif bmi <= 24.5:
    print(bmi)
    print("Normal weight")
elif bmi <= 29.9:
    print(bmi)
    print("Overweight")
else:
    print(bmi)
    print("Obese")   

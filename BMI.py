hight = float(input("enter your hight(m):"))
weight = float(input("enter your weight(kg):"))
bmi = weight/hight**2
print("bmi:" , bmi)
if bmi < 18.5:
    print("underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("normal")
elif bmi > 25 and bmi <29.9:
    print("overweight")
elif bmi > 24.9 and bmi < 30:
    print("obese")
elif bmi > 25:
    print("extremely obese")
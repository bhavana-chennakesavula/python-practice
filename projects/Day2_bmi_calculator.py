#BMI calculator
h = input("enter height in mts: ")
w = input("enter weight in kg: ")
height = float(h)
weight = float(w)
BMI = weight / (height ** 2)
if BMI < 18.5:
    print(" you are underweight")
elif BMI >=18.5 and BMI <25:
    print(" you have a normal weight")
elif BMI >= 25 and BMI <30:
    print(" you are overweight")
else:
    print(" you are obesed")
    
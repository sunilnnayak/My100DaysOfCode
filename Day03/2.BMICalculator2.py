# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.
# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

bmi=round(weight/height**2)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("slightly overweight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")
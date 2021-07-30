# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight = float(weight)
height = float(height)
bmi = round(weight / (height ** 2))
you = f"Your bmi is {bmi}. "
if bmi < 18.5:
    print(you + "You are underweight.")
elif bmi < 25:
    print(you + "You are normal weight.")
elif bmi < 30:
    print(you + "You are slightly overwieght.")
elif bmi < 35:
    print(you + "You are obese.")
else:
    print(you + "You are clinically obese!!!")

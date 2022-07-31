#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age?")
# 🚨 Don't change the code above 👆
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

years=90-int(age)
months=12*years
weeks=52*years
days=365*years
print(f"You have {days} days, {weeks} weeks, and {months} left")
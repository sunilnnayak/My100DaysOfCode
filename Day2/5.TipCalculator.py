# https://docs.python.org/3/tutorial/floatingpoint.html 
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

bill_tip= (tip/100*bill)+bill
total_bill=bill_tip/people
total=round(total_bill,2)
# total="{:.2f}".format(total_bill)
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
print(f"each person should pay {total}")
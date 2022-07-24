# write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill. 

#You are not allowed to use the `choice()` function.
# You might need the help of the `len()` function.

#Convert String to List in Python - https://www.askpython.com/python/string/convert-string-to-list-in-python

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# print(names)
import random
# print(random.choice(names))   #But we shouldn't use choice function

number_of_ppl= len(names)
payer=random.randint(0,number_of_ppl-1)
print(names[payer])



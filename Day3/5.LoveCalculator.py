# program that tests the compatibility between two people.

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number. 

# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 

# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."

# 1. The `lower()` function changes all the letters in a string to lower case. 
# (https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

# 2. The `count()` function will give you the number of times a letter occurs in a string. 
# (https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combined_string=name1.lower()+name2.lower()

T= combined_string.count('t')
R= combined_string.count('r')
U= combined_string.count('u')
E= combined_string.count('e')
first_num=T+R+U+E
L= combined_string.count('l')
O= combined_string.count('o')
V= combined_string.count('v')
E= combined_string.count('e')
sec_num=L+O+V+E

love_score=int(str(first_num+sec_num))

if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


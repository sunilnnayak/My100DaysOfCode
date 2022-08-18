############DEBUGGING#####################

# # Describe Problem (range func will not include 20. if range (1,21) prog will run)
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()

# # Reproduce the Bug ()   (list starts counting from 0. In randint(1.6) both 1 and 6 are included. As there is no list index of 6 it gives index out of range error.)
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# # Play Computer  (if we put year as 1994 code will not run. >= will solve this)
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors  (indentation is Print statement is missing. datatype of age is strings. In order to use it we should convert to int.and also print statement should be f string to use place holder)
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

# #Print is Your Friend (whenever stuck usr print statement to see what is inside the variable. Here == is a equala operator we have to use assgnment operator(=))
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(pages)
print(word_per_page)
print(total_words)

# #Use a Debugger (here for loop runs and at the end only 13*2=26 will be in new_item which will be stored in blist. So blist should be indented inside for loop to get entire data)
Online debugger : https://pythontutor.com/visualize.html#mode=edit

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])
# Day 4 (19/7/2022)

1. Random module-
https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
random_integer=random.randint(1,10)
print(random_integer)

random_float=random.random          --prints random from 0.00000-0.9999999
print(random_float)

random_float*5                      --prints random from 0.00000-4.9999999


2. Lists
# https://docs.python.org/3/tutorial/datastructures.html
fruits=["apple","banana","pear"]
print(fruits[0])               ---apple

fruits[1]= orange
print(fruits)                   ---["apple","orange","pear"]

fruits.append("fruit")           ---["apple","orange","pear"."fruits"]
                                     adds 1 item at the end of the list

IndexError:List index out of range
print(fruits[8])


3. Nested Lists 
fruits= ["apple","banana","pear"]
veggis= ["apple","banana","pear"]
total=[fruits,veggis]
print(total)            --- [["apple","banana","pear"],["apple","banana","pear"]]


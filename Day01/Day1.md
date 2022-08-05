# Day 1 (16/7/2022)

1. Comment in python
#
to comment multiple lines -- ctrl+/


2. print() function-
print("something")
 
print("hello\nworld")   --- \n to print in new line
print("hello"+"sunil")  --- output: hellosunil 
                            string concatination

    print("hello")      --- IndentationError


3. Python input function-
input("what is your name")

print("hello " +input("what is your name?"))   --- what is your name?Sunil
                                                    hello sunil

print(len("sunil"))           --- 5
print(len(input("what is your name? ")))     --- here we have 3 functions


4. Python Variables-
user_name=input("name?")
player1_username="sunil"
Variable name should not contain space.
Variable name should not start with number.
Variable name should not be a python kwywords like print, input, ...

#program to switch valuses stored in variable a and b
c=a
a=b
b=c
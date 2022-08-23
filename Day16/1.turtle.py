#https://docs.python.org/3/library/turtle.html
#import turtle
#timny = turtle.Turtle()   

#From turtle module get the Turtle class. In order to construct a object we need to add parenthesis at the end.
#Now save all of these into actual object which we named as Timny.

#We can simplyfy this code as
from turtle import Turtle,Screen
timny=Turtle()              # To create ne object from blueprint
print(timny)
timny.shape("turtle")       #here shape is a fuction of timny object also known as method.
timny.color("coral")       # this method changes color of the turtle 
timny.forward(100)          # this method moves turtle 


my_screen=Screen()
print(my_screen.canvheight)   # here canvheight is a attribute of a my_screen object
my_screen.exitonclick()      #here exitoclick is a fuction of my_screen object also known as method.

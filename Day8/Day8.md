# Day 8 (23/7/2022)

1. Functions with input

def my_function(something):
    #Do this with something
    #then do this
my_function(123)


Eg:
def greet(name):
    print(f"hello {name}")
    print(f"how do you do {name}")
   
greet("sunil")                    --here we are assigning argument("sunil") to parameter (name)



2. Positional and Keyword Arguments-
def greet(name,location):
    print(f"hello {name})
    print(f"what is ur {location}")

greet("sunil","udupi")
# This is positional parameter as the position of the argument matters


def greet(name,location):
    print(f"hello {name})
    print(f"what is ur {location}")

greet(location="udupi", name="sunil",)
# Keyword argument
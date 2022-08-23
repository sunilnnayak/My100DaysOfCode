# OOP
In OOP we try to model real life objects. And that object has things and they can do things.
(what it has and what it does)
or in other words - attributes (variable) and methods (function)


# Classes and Objects
Class is a blueprint
Objects are individual objects generated from blueprints
Example: If Waiter is a class, then Henry and Bettey (who are working as waiters in a Restuarent) can be objects.

# Constructing Objects and Accessing their attributes and Methods
Eg: car (object) , CarBlueprint (class)

car=CarBlueprint()
->We need to capitalize first letter of the word while naming class. This is called Pascal case. This is to differentiate all variables and function name (where each word is seperated by underscore).

In order to practice this functionality we can use library of code which someone else created like turtle
https://docs.python.org/3/library/turtle.html
1. Turtle.py

# Python Packages
To get the packages created by other developers: https://pypi.org/
Example prettytable package: https://pypi.org/project/prettytable/
2. Package.py


3. CoffeeMachineWithOOPs.py
MenuItem Class
Attributes:
    -  name
    (str) The name of the drink.
    e.g. “latte”
    - cost
    (float) The price of the drink.
    e.g 1.5
    - ingredients
    (dictionary) The ingredients and amounts required to make the drink.
    e.g. {“water”: 100, “coffee”: 16}

Menu Class
Methods:
    - get_items()
    Returns all the names of the available menu items as a concatenated string.
    e.g. “latte/espresso/cappuccino”
    - find_drink(order_name)
    Parameter order_name: (str) The name of the drinks order.
    Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
    otherwise returns None.

CoffeeMaker Class
Methods:
    - report()
    Prints a report of all resources.
    e.g.
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    - is_resource_sufficient(drink)
    Parameter drink: (MenuItem) The MenuItem object to make.
    Returns True when the drink order can be made, False if ingredients are insufficient.
    e.g.
    True
    - make_coffee(order)
    Parameter order: (MenuItem) The MenuItem object to make.
    Deducts the required ingredients from the resources.

MoneyMachine Class
Methods:
    - report()
    Prints the current profit
    e.g.
    Money: $0
    - make_payment(cost)
    Parameter cost: (float) The cost of the drink.
    Returns True when payment is accepted, or False if insufficient.
    e.g. False

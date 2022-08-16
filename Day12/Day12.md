# Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")     ---2

increase_enemies()
print(f"enemies outside function: {enemies}")      ---1

# Local scope
def drink_potion():
    potion_strength=2
    print(potion_strength)      ---2

drink_potion()
print(potion_strength)          ---Error  (Nameerror: 'Potion_strength' is not defined)

#when we create new variable/function inside a function it can only be accesible inside that function.

# Global scope
player_health=10           #global variable
def drink_potion():
    potion_strength=2       #Local variable
    print(player_health)      ---10

drink_potion()
print(player_health)          ---10

#Global variables are accesible with and outside the function


# Does Python have block scope? 
Answer: No
eg:
game_level=3
enemies=['Skeleton','Zombie','Alein']
if game_level>5:
    new_enemy=enemoes[0]
print(new_enemy)

#This is completely valid and code works. 

#if we create varible within a function then it will only be available within that function
#But if we create a variable within a if block/while loop/for loop or anything that has indentation/colon then that doesnot count as creating separate local scope.

# How to modify global scope
enemies = 1

def increase_enemies():
  enemies = 2                                   #here we are not modifying ealier variable but creating new variable
  print(f"enemies inside function: {enemies}")     

increase_enemies()
print(f"enemies outside function: {enemies}")      


#Now
enemies = 1

def increase_enemies():
  global enemies                        # with this we can bring global variable into local scope and modify it
  enemies +=1
  print(f"enemies inside function: {enemies}")     

increase_enemies()
print(f"enemies outside function: {enemies}")      

#But this is not at all recomemded.
#because it is confusing and can create bugs. Beacuse this global scope can be created anywhere in the code. And we are modifying it later.
#We cab read the global scope in a local scope, we can use it but do not try to modify it within a function that has local scope.
#Instead, we could use return statement
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")  
  return enemies+1   

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")    

# Global constants
the variable which we define and we never change it again. In order to differentiate these constants which we are never going to change we, the naming convention is to change it into all upper case. That means later on in our function when we use these constants it reminds us not to change its value.
eg:
PI=3.14
URL='https://"
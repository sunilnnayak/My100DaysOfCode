#Number Guessing Game Objectives:

# Include an ASCII art logo.  http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print (logo)
computer_guess=random.randint(1,101)
print(computer_guess)
print('Welcome to number Guessing Game!')
print('I am thinking of a anumber between 1 and 100')

guess_count=0

def diff_level():
    difficulty=input('Choose a difficuty. Type "easy" or "hard": ').lower()
    if difficulty == 'easy':
        guess_count=10
        print(f'You have {guess_count} attempts remaining to guess the game')
    elif difficulty == 'hard':
        guess_count=5
        print(f'You have {guess_count}  attempts remaining to guess the game')
    else:
        print('please enter valid input')
diff_level()

user_guess= int(input('Make a guess: '))
def game_begins():
    if user_guess>computer_guess:
        print('Too high')
        print('Guess again')
        guess_count-=1
    print(f'you have {guess_count} attempts remaining to guess the number')

    if user_guess<computer_guess:
        print('Too low')
        print('Guess again')
        guess_count-=1
    print(f'you have {guess_count} attempts remaining to guess the number')

    if user_guess==computer_guess:
        print('You guessed the number ')
        print(f'The number was {computer_guess}')

game_begins()
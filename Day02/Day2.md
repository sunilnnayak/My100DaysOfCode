# Day 2 (17/7/2022)

1. Python Primitive Datatypes

String 
print("hello"[0])     --- h     ,subscript
print("hello"[4])     --- o

Integer
print(123+345)      --- 468
print(123_456_789)          ---123456789 , (Large integers), we can use _for comma

Float
3.14159

Boolean
True
False


2. Type error,type checking, type conversion
len(4876)       ---TypeError: object of type 'int' has no len()


num_char=len(input("what is ur name"))
print("UR name has "+num_char+ "charecter")   ---TypeError:can only concatenate str (not 'int') to str


num_char=len(input("what is ur name"))
print(type(len(input("what is ur name"))))     --- <class 'int'>   , type checking



num_char=len(input("what is ur name? "))          ---what is ur name? Sunil
new_num_char=str(num_char)                          ---(type conversion)
print("UR name has "+ new_num_char+ "charecter")   --- UR name has 5 charecter


a=123
print(type(a))      --- <class 'int'>
a=str(123)
print(type(a))      --- <class 'str'>


print(70 + float("100.5"))      ---170.5
print(str(70) + str(100))          ---70100


3. Mathematical Operations
3+5     --ADD
7-4     --SUB
3*2     --MUL
6/3     --DIV (output- 2.0  , we get float)
2**2    --EXPONENT (4)

BODMAS rule
()
**
*,/             - Calculation goes from left to right
+,-


4. Number manupulation and F Strings
print(8/3)      --2.66666666666
print(int(8/3))     --2
print(round(8/3))   --3   (using round function)
print(round(8/3,2))     --2.67
print(8//3)         --2

print(type(8/3))    --<class 'float>
print(type(8//3))   --<class 'int'>

score = 0
score += 1
print(score)        --1


score=0
height=1.8
isWinning=True
print(f"your score is {score}, height is {height}, winning {true}")     --your score is 0, height is 1.8, winning True


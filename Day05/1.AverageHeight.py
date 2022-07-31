# write a program that calculates the average student height from a List of heights. 
# You should not use the `sum()` or `len()` functions in your answer.
# Remember to use the `round()` function to round the average height before you print it.

student_heights = input("Input a list of student heights ").split()
# print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#   print(student_heights)
# 🚨 Don't change the code above 👆

total_height=0
count=0
for height in student_heights:
    total_height +=height
# print(total_height)

for student in student_heights:
    count+=1
# print (count)


average=round(total_height/count)
print(average)
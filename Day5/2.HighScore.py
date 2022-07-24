# program that calculates the highest score from a List of scores.
# e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`
# you are not allowed to use the max or min functions.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# print(max(student_scores))      -- easy, but we canot use as per interviwer

highest=student_scores[0]
for score in student_scores:
    if score>highest:
        highest=score
print(highest)
# Write a program to display marks of 10 students using dictionary.
d = dict()
for i in range(1, 11):
    print ("Enter marks of student", i)
    marks = int(input())
    d[i] = marks
print("Marks of students are:")
for i in range(1, 11):
    print("Marks of student" ,i ,"is", d[i])    
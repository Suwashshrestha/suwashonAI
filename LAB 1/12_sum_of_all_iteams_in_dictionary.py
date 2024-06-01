d={'a': 100, 'b':200, 'c':300}
for i in range(0,3):
    n=int(input("Enter a number:"))
    d[i]=n
sum=0
for i in d:
    sum=sum+d[i]
print("Sum of all the items in the dictionary is:", sum)

list = [0, 0, 0, 0, 0]
for i in range(0, 5):
    number = int(input("Enter a number: "))
    list[i] = number
sum = 0
for i in range(0, 5):
    sum = sum + list[i]
print("Sum of all elements in the list is:", sum)

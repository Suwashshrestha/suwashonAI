
dict = {}
n = int(input("Enter number of items in dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict[key] = value
sum = 0
for i in dict:
    sum = sum + dict[i]
print("Sum of all items in dictionary is:", sum)




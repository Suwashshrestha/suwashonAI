list = [0,0,0,0,0,0,0,0,0,0]
largest =0
for i in range(0, 10):
    n = int(input("Enter a number:"))
    list[i] = n

for i in range(0, 10):
    if list[i] > largest:
        largest = list[i]
print("The largest number is", largest)

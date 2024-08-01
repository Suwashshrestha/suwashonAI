list = [12,4,11,13,51]


print("List before sorting:",list)
for i in range(0,5):
    for j in range(i+1,5):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("List after sorting:",list)


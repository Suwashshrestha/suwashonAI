import math

n=100  
for i in range(2,n+1):  
    isprime = 1 
    for j in range(2,i//2+1):  
        if(i%j==0):  
            isprime=0  
            break 
    if isprime==1:  
        print(i, end=" ");  
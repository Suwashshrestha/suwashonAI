print('enter two number')
num1 = int(input())
num2 = int(input())

def fun(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quotients = num1 / num2
    return sum, diff, prod, quotients   
print(fun(num1, num2))

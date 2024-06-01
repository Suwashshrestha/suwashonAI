print('please enter percentage to dispay it in division format')
percent = int(input())
if percent >= 80:
    print('Distinction')
elif percent >= 60:
    print('First Division')
elif percent >= 40:
    print('Second Division')
else:
    print('Fail')
    
#swap case of all characters in a string
str=input("Enter a sentence: ")
str1=""
for i in str:
    if i.islower():
        str1+=i.upper()
    else:
        str1+=i.lower()

print("The sentence after converting all lowercase characters to uppercase is:",str1)

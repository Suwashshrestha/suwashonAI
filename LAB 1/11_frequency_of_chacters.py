str=input("Enter a sentence: ")
freq={}
for i in str:
    frequency = str.count(i)
    freq[i]=frequency
print("Frequency of all characters in the sentence is:",freq)

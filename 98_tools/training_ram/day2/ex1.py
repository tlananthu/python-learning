#count vowels

word=input("Enter a word: ")

var=0
for i in word:
    if i in "aeiouAEIOU":
        var+=1
        print(i)

print("Vowels count=",var)
#sorted list of vowels

word=input('Enter a word: ')

var=[]
for i in word:
    if i in "aeiouAEIOU":
        var.append(i)

var.sort()
print(var)

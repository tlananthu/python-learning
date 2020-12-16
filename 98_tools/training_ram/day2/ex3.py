#list of vowels

# word=input('Enter a word: ')

# filtered=""

# for i in word:
#     if i in "aeiouAEIOU":
#         filtered+=i

# print(filtered)

word=input('Enter a word: ')

var=[]
for i in word:
    if i in "aeiouAEIOU":
        var.append(i)
print(var)
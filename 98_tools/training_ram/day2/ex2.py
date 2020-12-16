#filter vowels

word=input('Enter a word: ')

filtered=""

for i in word:
    if i not in "aeiouAEIOU":
        filtered+=i

print(filtered)
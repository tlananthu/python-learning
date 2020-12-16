#print index of all odd numbers
l=eval(input('Enter a list of numbers: '))

for i in l:
    if i%2==0:
        print(i)

#print([i if i%2==0 else 0 for i in l])




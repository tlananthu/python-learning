# WAP to check if a given password has a mix of letters and digits.

#     >>> practiceQuestion('abc12ed')
#     True
#     >>> practiceQuestion('abcd')
#     False
#     >>> practiceQuestion('1234')
#     False
    

#isalpha
#isdigit
#islnum
from getpass import getpass
p=getpass("Enter password: ")
alpha = num = 0
for l in p:
    if l.isalpha():
        alpha+=1
    elif l.isdigit():
        num+=1
print(alpha>0 and num>0)


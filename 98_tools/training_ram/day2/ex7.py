#label encoder

#input list
#['Yes','NO','yes','YES','no']
#output
#[1,0,1,1,0]
#1 for yes, 0 for no

# l=eval(input("Enter list: "))
# nl=[]

# for i in l:
#     if i.upper()=="YES":
#         nl.append(1)
#     elif i.upper()=="NO":
#         nl.append(0)

#updated with ternary
l=eval(input("Enter list: "))
nl=[]
for i in l:
    nl.append(1 if i.lower()=='yes' else 0)

print(nl)

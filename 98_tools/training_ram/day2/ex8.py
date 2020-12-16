#list comprehension
#label encoder

#input list
#['Yes','NO','yes','YES','no']
#output
#[1,0,1,1,0]
#1 for yes, 0 for no
l=eval(input("Enter list: "))

nl=[1 if i.lower()=="yes" else 0 for i in l]
print(nl)
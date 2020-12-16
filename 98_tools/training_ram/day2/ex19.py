
li=[12,12]
# val=0
# if len(li)>1:
#     val=li[0]+li[-1]
# elif len(li)==1:
#     val=li[0]

# print(val)

def q1(l=None):
    if len(l)==0:
        return 0
    elif len(l)==1:
        return l[0]
    else:
        return l[0]+l[-1]

q1([])
q1([10])
q1([10,20])

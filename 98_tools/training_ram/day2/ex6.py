#find common data in two given lists, output in sorted form

# first=eval(input("First: "))
# second=eval(input("Second: "))

# common=[]
# for f in first:
#     for s in second:
#         if f==s:
#             common.append(f)
#             break

# print(sorted(common))

#updated
first=eval(input("First: "))
second=eval(input("Second: "))
common=[]
for f in first:
    if f in second:
        common.append(f)
print(sorted(common))
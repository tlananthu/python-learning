# steps in file handling

# open file and make file object
# read or write operation
# close the file

#98_tools\training_ram\day3\plainfile.txt

# file object has following attributes
# f.name, f.mode, f.encoding, and some attributes about file

# open(filename, mode), opens the file
#   mode is either r,w,a for generic
    #   rt, wt, at for text file
    #   rb, wb, ab for binary file
    #   default is r
# readable(), if file is readable
# writable(), if file is writable
# read(), read all content as single string object
# readline(), reads one line from current cursor location
# readlines(), reads all lines as list object, with each line as string
# write(str), pass string object to file
# writelines(list), writes the given list (of string objects) object to file
# close(), close the file object
# closed(), true/false to check if file is closed
# with: context manager
# tell(), tells the current cursor index (with 0 based index)
# seek(index): moves the cursor to given index

# read mode sets cursor at the beginning of file, append sets the cursor at the end of file
# both write and append creates the file if not found

# f=open(r'98_tools\training_ram\day3\plainfile.txt', 'rt')
# print(f.readable())
# print(f.writable())
# print(f.read())
# f.close()
# print(f.closed)

# f=open(r'98_tools\training_ram\day3\plainfile.txt', 'rt')
# print(f.readable())
# print(f.readable())
# print(f.read()) #reads from current cursor position till end of file
# f.close()


#copy the contents of text file into another
# f=input('Enter file name: ')+'.txt'
# nf=input('Enter new file name: ')
# f=open(f)
# if f.readable():
#     g=open(nf,'w')
#     if g.writable():
#         g.write(f.read())
#         g.close()
# f.close()

with open(r'C:\Users\ananthan\Documents\PYthonLearn\98_tools\training_ram\day3\plainfile.txt') as f:
    print(f.read())
print(f.encoding)







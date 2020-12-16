# ids = ['id1','id2','id32','id23','id9']
#lex sort is sorted on alpha
#do an integer sort

#ids = ['id1','id2','id32','id23','id9']
#print((lambda x:x[2:], ['id1','id2','id32','id23','id9']))

print(sorted(['id1','id2','id32','id23','id9'], key=lambda x:int(x[2:])))




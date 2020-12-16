
d={2011:74, 2012:64, 2013:78, 2014:36, 2015:57}

#find in which year it was max
val=0
year=0

for k,v in d.items():
    if v==max(d.values()): print(k)
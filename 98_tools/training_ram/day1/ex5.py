#leap year

'''
year%4 -> Leap
year%100 -> not Leap
year%400 -> Leap
'''

year=int(input('Year: '))

status="Leap" if year%4==0 and year%100!=0 or year%400==0 else "Not Leap"
print(status)


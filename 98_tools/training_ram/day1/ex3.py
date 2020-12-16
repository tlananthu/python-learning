#pythagorean theorem

#hypoteneus=square root of base^2+height^2
#3,4->5.0

from math import sqrt

base=eval(input('Enter Base: '))
height=eval(input('Enter Height: '))

hyp=sqrt(base**2 + height**2)

print(hyp)
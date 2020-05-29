x = [1, 2, 3]
def func(x):
    print(x)
    x[1] = 42  # this changes the caller!
    print(x)
    x = 'something else'  # this points x to a new string object
    print(x)

func(x)
print(x)  # still prints: [1, 42, 3]
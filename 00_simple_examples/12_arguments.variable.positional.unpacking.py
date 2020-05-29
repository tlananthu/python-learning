# arguments.variable.positional.unpacking.py
def func(*args):
    print(args)
    print(type(args))

values = (1, 3, -7, 9)
func(values)   # equivalent to: func((1, 3, -7, 9))
func(*values)  # equivalent to: func(1, 3, -7, 9)
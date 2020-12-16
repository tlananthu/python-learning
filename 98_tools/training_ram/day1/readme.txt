DAY 1
-----
packages - files folders
module - python code

1. simple and readable
2. open source & communities
3. Interactive **.py or >>>)
4. Interpreted (compiled and then interpreted)
	compiled checks for syntax errors (syntax errors wont pass)
	logical errors will pass compilation (1/0 etc)
5. object oriented but not imposed
6. case sensitive
7. Implicitly defined
8. dynamically typed
	def add(a,b):
		return a+b
	add(2,3)
	add(1.1,4)
	add('a','dsdf')
	add([1,1,1],[3,3,3])

type(var)
dir(var) attributes of a particular object, namespace
help(str) built in documentation

automate the boring stuff
r'' -> raw string
""" -> multiline string/docstring
dir(__builtins__)

keywords
	import keyword
	print(keyword.kwlist)

take input: console, file, databases, socket, 
processing: control flow
publish:

Arithematic operators:
    + - / *
    //: floor divide (get the integer division)
    %: modulus (get the remainder of division)
    **: exponent
    round(10/3,2)

operator precendence tier:
    ()
    **
    * / // %
    + -
    within same tier its Left to Right

data types:
    - Number - int, float, complex

    i=28497897389273897289572893475982347897234857283475823452452345234
    import sys
    sys.getsizeof(i)

    - String
    Collections: (ordered by index)
    - List []
        [1,2,3]
    - Tuple ()
        - is a read only list (immutable list)
        (1,2,3)
    Dictionary (dict) {}
        unordered by index
        {0:'Apple', 1: 'Bat'}

        {0:'Apple', 1: 'Bat'} == {1: 'Bat', 0:'Apple'}
    Set {} 
        unique list of items

    Typecasting:
        int(), float(), complex()
        str()
        list()
        dict()
        set()
        universal: eval()

Control flow:
    Conditions, Ternary Operator, List comprehension
    in, not in, and, or

    Ternary operator:
        True if condition else False

seaborn library for maps python

DAY 2
-----
sort() on a list acts on mutable list and does not return anyhthing

__add__() #read as dunder add

dir(list)

__ is added to prevent accidental overwriting of builtin functions


#set
-mutable collection of immutable values
    set is mutable, the collection can change, but the values in the collection cannot change
    {(1,2),3,'a'} #possible
    {1,2,[3,4]}#not possible 
    -set is a unique collection
    -set is a collection of immutable items only.
    -set is mutable
-intersection
-union
-difference
-symmetric difference


when to chose what:
    -mutable+redundant:list
    -immutable+redundant:Tuple
    -mutable+unique:set
    -immutable+unique:frozenset

#Dictionary
-mutable and unordered collection as key:value pair
-denoted by {}

#comprehension
-shortcuts in python
    -list comprehension
        -One liner shortcut for creating a list object from any iterable by mapping or filtering or both
        [expression for loop]
        or
        [expression for loop if condition]
        
        def square(x):
            return x**2

        s=[1,2,3,4,5,6,7,8,9]
        map(square,s) #lazy processing

        list(map(square,2))#retuns a list with square applied on each item

        #[condition for (if)]
        l=[1,2,3,4,5]
        [i**2 for i in l]
        [i for i in l if i%!=0]

    -Dictionary comprehension
        {key_exp:value_expr forloop condition}

        x='india'
        {i:word.count(i) for i in "aeiouAEIOU"}

        s='Some text with spaces'
        x=s.split()
        {i:x.count(i) for i in x}

lambda functions
    shortcut for writing functions
    lambda is a keyword like def to create a function object
    lambda function can be anonymous
    lambda is a one liner shortcut for functions 
        simplicity/readable
        maybe efficient sometimes
    lambda args:expression    #no need for paranthesis
    
    def add(a,b): return a+b
        can be written as
    add = lambda a,b: a+b

    even = lambda num: num%2==0

    even_odd = lambda num: "Even" if c%2==0 else "Odd"

    print(list(map(lambda x:x**2, [1,2,3,4,5])))

    print(list(map(lambda x:x%2==0, [1,2,3,4,5])))

    (lambda x: x+1)(2)

    (lambda x: x%2 and "Odd" or "Even")(2)

    list(map(lambda x:x.upper(), ['anil','Rohan','RAKESH']))


Overloading function:

def add(*args):
    return sum(args)

add()
add(1)
add(1,2,3)

Monday
------
file
    
exception
mini project





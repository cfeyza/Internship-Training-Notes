numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

name = "Kali Linux"
for n in name:
    print(n)

tuple = (1,2,3,4,5)
for t in tuple:
    print(t)
tuple = [(1,2),(3,4),(5,6)]
for t,z in tuple:
    print(t,z)

d = {"k1":1, "k2":2, "k3":3}
for i in d:
    print(i)
for i in d.items():
    print(i)
for k,i in d.items():
    print(k, i)

greeting = "Hello"
for index, letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")
for item in enumerate(greeting):
    print(item)

list1 = [1,2,3,4,5]
list2=["a","b","c","d","e"]
print(list(zip(list1,list2)))

list3 = ["x","y","z","w","q"]
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

numbers = [x for x in range(10)]
numbers = [x**2 for x in range(10)]
numbers = [x**x for x in range(10) if x%3 ==0]

results = [x if x%2 ==0 else "TEK" for x in range(1,10)]

result =[]
for x in range(3):
    for y in range(3):
        result.append((x,y))

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
list1 = [1,2,3,4,5]
list2 = list1[:] #slicing farklı listeler oluşturur

def my_func(*params):
    print(params)
    sum=0
    for i in params:
        sum += i
    return sum

def displayUser(**kwargs):
    for key,value in kwargs.items():
        print("{}is {}".format(key,value))

def my_Func(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

my_Func(10,20,30,40,50,key1="value", key2="value")

#LAMBDA MAP FILTER
def square(num): return num**2
numbers = [1,3,5,9]
print(list(map(square, numbers)))
print(list(map(lambda num: num**2, numbers)))
cube = lambda num: num**3
print(list(map(cube, numbers)))

numbers = [1,3,5,6,9,10]
def check_even(num) : return num%2==0

print(list(filter(check_even, numbers)))
print(list(filter(lambda num: num%2==0, numbers)))
check_odd = lambda num: num%2!=0
print(list(filter(check_odd, numbers)))


#OOP Object Oriented Programming
#class #instance(object)

class Person:
    pass
#constructor
#def __init__()
    #attributes
    #methods

p1 = Person
p2 = Person
print(p1==p2)


#MATH MODULU
import math
value = dir(math)
print(value)
value = help(math)
print(value)

import math as islem
from math import *
from math import factorial,sqrt

import random
result = random.random() #0.0 - 1.0
result = random.uniform(10,100)
result = random.randint(1,100)
my_list = ["a","b","c","d"]
result = random.choice(my_list)

liste = list(range(10))
random.shuffle(liste) #otijinal liste değişir

liste = range(100)
result = random.sample(liste, 3)

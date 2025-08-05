def greeting(name):
    print("hello", name)

print(greeting)
sayHello = greeting
print(sayHello)

del sayHello
print(greeting)
#print(sayHello)


#encapsulation
def outer(num1):
    print("outer")
    def inner(num):
        print("inner")
        return num+1
    num2 = inner(num1)
    print((num1,num2))
#inner sadece outer kapsamında çalışır
outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)

    return inner_factorial(number)
try:
    print(factorial(-2))
except Exception as ex:
    print(ex)

def usalma(number):
    def inner(power):
        return number**power
    return inner

two = usalma(2)
print(two(3))

#fonksiyona parametre olarak fonksiyon adı gönderme
def toplam(*args):
    print("toplam called")
    sum = 0
    for i in args:
        sum+=i
def carpim(*args):
    print("carpim called")
    product = 1
    for i in args:
        product *= i

def islem(f1,f2, islem_adi):
    if islem_adi == "toplam":
        print(f1(2,3))
    elif islem_adi == "carpim":
        print(f2(2,3))
    else:
        print("Error")


#bir fonksyiona bir özellik eklemek istediğimizde decorator fonksiyon kullanılır
#bir özellliği birden çok fonksiyona eklemek istediğimizde

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

sayHello()
sayHello = my_decorator(sayHello)
sayHello()

#decorator bu şekilde çağrılır
@my_decorator
def sayGreeting():
    print("greeting")

sayGreeting()

#eğer parametre varsa
def my_decorator(func):
    def wrapper(param):
        print("before")
        func(param)
        print("after")
    return wrapper

@my_decorator
def sayName(name):
    print("hello",name)

sayName("ali")

#Fonksiyonların ne kadar sürede çalıştığını hesaplayan decorator
import time
def chrono(func):
    def wrapper(*args, **kwargs):
        t0 = time.time() #now
        time.sleep(1) 
        func(*args, **kwargs)
        tf = time.time()
        print(f"Function {func.__name__} finished in {str(tf-t0)}")
    return wrapper

from math import pow,factorial
def usalma(a,b):
    print(pow(a,b))

#chrono(usalma(2,3)) bu çalışmıyor

@chrono
def faktoriyel(num):
    print(factorial(num))

faktoriyel(4)
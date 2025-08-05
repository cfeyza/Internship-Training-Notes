my_list = ["♥","♦","♣","♠"]
iterator = iter(my_list)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

for i in my_list:
    print(i)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

class MyRange:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start+=1
            return x
        else:
            raise StopIteration

        
my_range = MyRange(20,50)
for i in my_range:
    print(i)

my_range2 = MyRange(1,5)   
myiter = iter(my_range2)
print(next(my_range2))

#Generator, bir iterator objesi oluşturmak için kullanılır
#Generator, bellekte yer işgal etmeyen bir iterator üretir

def cube():
    for i in range(5):
        yield i**3
        #bellekte bir yere atanmaz, üretildiği anda kullanıcıya sunulur

print(cube())
iterator = iter(cube())
print(next(iterator))
print(next(iterator))
print(next(iterator))
#ya da
print(next(cube()))
print(next(cube()))
#fonksiyonun kendisi bir iterator olduğu için
iterator_orig = cube()
print(next(iterator_orig))
print(next(iterator_orig))
print(next(iterator_orig))

for i in iterator_orig:
    print(i)

liste = [i**3 for i in range(5)] #generator objesi
print(liste)
liste = (i**3 for i in range(5)) #generator objesi
print(next(liste))
print(next(liste))

for i in liste:
    print(i)
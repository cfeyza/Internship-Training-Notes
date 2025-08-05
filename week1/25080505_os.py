import os
print(dir(os))

x = os.name
print(x)
x = os.getcwd
print(x)
os.mkdir("osExapmles")
os.chdir("osExamples")
#os.chdir("..")
#os.chdir("../..")
#os.chdir("C:/")
os.makedirs("newDirectory1/newDirectory2")
os.rename("newDirectory1","newDirectory")
os.rmdir("NewDirectory2")
os.removedirs("newDirectory/newDirectory2")
x = os.listdir()
print(x)
x = os.listdir("C:/")
print(x)

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
x = os.stat("newfile.py")
#st_size : byte cinsi boyut
#st_atime : son erişilme zamanı
#st_mtime : son değiştirilme tarihi
#st_ctime : oluşturulma zamanı
print(x.st_size/1024) #KB
from datetime import datetime
#print(datetime.fromtimestamp(x.st_ctime)) ctime deprecated
print(datetime.fromtimestamp(x.st_birthtime)) #ctine yerine
print(datetime.fromtimestamp(x.st_atime))
print(datetime.fromtimestamp(x.st_mtime))

os.system("notepad.exe")

x = os.path.abspath("_os.py")
x = os.path.dirname('C:/Users/FEYZA/OneDrive/Belgeler/python_august/_os.py')
x = os.path.dirname(os.path.abspath("_os.py"))

x = os.path.exists("_os.py")
x = os.path.exists("c:/Users") #Var mı?

x = os.path.isdir("C:/Users") #Klasör mü
x = os.path.isfile("C:/Users") #Dosya mı

x = os.path.join("C:/","notexistingdir","notexistingdir2") #Dosyalar yok ama yol parçaları birleşti
x = os.path.split("C:/Users/FEYZA/OneDrive/Belgeler/python_august")
x = os.path.splitext("_os.py") #dosya ismi ve uzantısını ayırıp listeye atar
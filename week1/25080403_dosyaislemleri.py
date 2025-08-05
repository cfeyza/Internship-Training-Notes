file = open("newfile.txt","w")
file.close()

file = open("newfile.txt", "w", encoding='utf-8')
file.write("Hello World")
file.close()

try:
    file = open("newfile.txt", "r", encoding='utf-8')
    print(file)
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı")
    file.close()

#for ile
for i in file:
    print(i, end='')

#read() fonk ile
content = file.read()
print(content)

content = file.read(5) #kaldığı yerden okumaya devam  eder

#readline() fonk

print(file.readline(), end='')

liste = file.readlines()
print(liste)

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

file.tell() #imlecin konumunu söyler
file.seek(10) #imleci 10. konuma gönderir

#SAYFA GÜNCELLEME

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())

#SAYFA SONUNDA GÜNCELLEME
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nnewline")

#SAYFA BAŞINDA GÜNCELLEME
with open("newfile.txt","a",encoding="utf-8") as file:
    content = file.read()
    content = "newline\n" + content
    file.seek(0)
    file.write(content)

#SAYFA ORTASINDA GÜNCELLEME
with open("newfile.txt","a",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "\nnewline\n")
    print(list)
    for i in list:
        file.write(i)
    #file.writelines(list)
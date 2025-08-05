import re
print(dir(re))

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

x = re.findall("Python", str)
x = len(x)

x = re.split(" ",str)

x = re.sub("\s","-",str)

x = re.search("Python",str)

print(x.span())
print(x.start())
print(x.stop())
print(x.end())
print(x.group())
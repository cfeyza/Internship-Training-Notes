import re

txt = "The rain in Spain"
#Print a list of all matches:
x = re.findall("ai", txt)
print(x)
#Return an empty list if no match was found:
x = re.findall("Portugal", txt)
print(x)
#Search for the first white-space character in the string:
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
#Make a search that returns no match:
x = re.search("Portugal", txt)
print(x)
#Split at each white-space character:
x = re.split("\s", txt)
print(x)
#Split the string only at the first occurrence:
x = re.split("\s", txt, 1) 
print(x)
#Replace every white-space character with the number 9:
x = re.sub("\s", "9", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)
#Do a search that will return a Match Object:
x = re.search("ai", txt)
print(x) #this will print an object
#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.span())
#Print the string passed into the function:
x = re.search(r"\bS\w+", txt)
print(x.string)
#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.group())
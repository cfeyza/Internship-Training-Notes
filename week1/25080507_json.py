import json
person_str = '{"name":"Ali", "languages":["python","C#"]}'

#JSON str to dict
result = json.loads(person_str) #dictionaryye load eder
print(result["name"])
print(type(result))
#Dosyadan JSON Okuma
with open("person.json") as f:
    data = json.load(f) #dataya jsonu aldık
    print(data["name"])
    print(type(data))

person_dict = {"name":"Ali", "languages":["python","C#"]}
#Dict to JSON
result = json.dumps(person_dict)
print(result)
print(type(result)) #dict artık str oldu
#Dosyaya str olarak kaydetmek
with open("person.json", "w") as f:
    data = json.dump(person_dict, f)

cars_str = '{"model1" : 2000, "model2" : 3000}'
cars_dict = json.loads(cars_str)
print(cars_dict)
cars_show_Str = json.dumps(cars_dict, indent=4, sort_keys=True)
print(cars_show_Str)
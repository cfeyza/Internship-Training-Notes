import json
print(json.__file__)

import requests
#bu modülle http request yapılabiliyor
#web sitesine talep bu modülle yapılıyor

result = requests.get("https://jsonplaceholder.typicode.com/todos")
print(result) #200 başarılı demek
print(type(result))
result_text = result.text
print(type(result_text))
json_dict = json.loads(result_text)
print(json_dict[0]["title"])
print(json_dict)
for i in json_dict:
    print(i["title"])

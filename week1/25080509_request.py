import requests
import json
api_key ="2f388569821df874b4ae2105"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

cashIn = input("From ? : ")
cashOut = input("To ? : ")
cashAmount = float(input("how much ? : "))

result = requests.get(api_url + cashIn)
result_dict = json.loads(result.text) #İsteğin metnini dict olarak gönder

print(
f"""1 {cashIn} = {result_dict['conversion_rates'][cashOut]} {cashOut}
{cashAmount} {cashIn}= {result_dict['conversion_rates'][cashOut]*(cashAmount):.3f} {cashOut}"""
)


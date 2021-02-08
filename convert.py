import requests
import json
import http_utility



print('This application currently supports:')
list_of_currency = requests.get('https://api.exchangeratesapi.io/latest')
c_list = json.loads(list_of_currency.text)
for i in c_list['rates'].keys():
    print(i)
curr_1 = input('Please write the currency you are converting from(ex: USD, EUR, etc.):')
curr_2 = input('Now write the currency you are converting to:')

rate = http_utility.get_conversion_rates(curr_1, curr_2) #base needs to be in request, so only need one method
price = json.loads(rate)['rates']

conversion = price[curr_2]
amount = float(input('Please input the amount of currency you wish to convert'))



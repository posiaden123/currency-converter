import requests

def get_conversion_rates(r1, r2):
    url = f'https://api.exchangeratesapi.io/latest?base={r1}&symbols={r2}'
    return requests.get(url).text

import requests
DATA_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.104"}

def get_ex_data():
    response = requests.get(DATA_URL, headers=headers)
    json_data = response.json()
    return json_data


def search(cc_key, data):
    for element in data:
        if element['cc'] == cc_key:
            return element


def get_rate_by_cc_key(cc_key):
    data = get_ex_data()
    element = search(cc_key, data)
    return element['rate']


def exchange(_id, amount):
    if _id == 1:
        rate = get_rate_by_cc_key('USD')
        return round(amount * float(rate), 2)
    elif _id == 2:
        rate = get_rate_by_cc_key('EUR')
        return round(amount * float(rate), 2)
    elif _id == 3:
        rate = get_rate_by_cc_key('USD')
        return round(amount / float(rate), 2)
    elif _id == 4:
        rate = get_rate_by_cc_key('EUR')
        return round(amount / float(rate), 2)
    else:
        return 'Unknown id'

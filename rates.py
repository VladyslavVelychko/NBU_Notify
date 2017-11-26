import ast
import datetime
import requests


def fetch_nbu_currency():

    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

    querystring = {"valcode": {"CAD", "USD", "EUR"}, "date": datetime.date.today().strftime('%Y%m%d'), "json": ""}
    cur_dict = {}

    for i in querystring["valcode"]:
        querystring["valcode"] = i
        response = requests.get(url, params=querystring)
        lst = ast.literal_eval(response.text)
        cur_dict[lst[0]['cc']] = lst[0]['rate']
    return cur_dict

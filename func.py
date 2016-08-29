# -*- coding: utf-8 -*
# file to store functions
# For developers only.  If you are admin user kindly check config.py

import random
import json
import config
import xml.etree.cElementTree as ET
from urllib.request import urlopen, URLError

# to parse astrology data
def astro(s):
    try:
        resp = urlopen(config.astroURL)
    except URLError:
        return "Звезды молчат"

    tree = ET.ElementTree(file=resp)
    root = tree.getroot()
    root.tag, root.attrib
    today = str(root[s][1].text)
    tomorrow = str(root[s][2].text)
    return "%s А вот завтра будет: %s" % (today, tomorrow)

#to parse weather status
def weather():
    try:
        resp = urlopen(config.weatherURL)

    except URLError:
        return "Обновление погоды..."

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    temp_c = data['current_observation']['temp_c']
    status = data['current_observation']['weather']
    humidity = data['current_observation']["relative_humidity"]
    return "Температура в %s сейчас %s C \n %s \n Влажность %s" % ("Киеве", temp_c, status, humidity)

#to parse hrivnta exchange rate from Yahoo
def yahooFinance():
    try:
        resp = urlopen(r"https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22USDUAH,EURUAH%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
    except URLError:
        return "Курс уточняется : Yahoo"

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    rate_usd = string_to_float(data['query']['results']['rate'][0]['Rate'])
    rate_eur = string_to_float(data['query']['results']['rate'][1]['Rate'])
    return "$%s за доллар и EUR%s: Yahoo" % (rate_usd, rate_eur)

#to parse hrivna exchange rate from Privat Bank
def privatBankFinance():
    try:
        resp = urlopen(r"https://api.privatbank.ua/p24api/pubinfo?json&exchange")
    except URLError:
        return "Курс уточняется : Приват"
    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    try:
        rate_eur_buy = string_to_float(data[0]['buy'])
        rate_eur_sale = string_to_float(data[0]['sale'])
        rate_usd_buy = string_to_float(data[2]['buy'])
        rate_usd_sale = string_to_float(data[2]['sale'])
    except IndexError:
        return "Курс уточняется : Приват"

    return "$%s/%s, EUR %s/%s: Приват" % (rate_usd_buy, rate_usd_sale, rate_eur_buy, rate_eur_sale)

#to parse hrivna exchange rate from UkrSibBank Bank
def UkrSibBankFinance():
    try:
        resp = urlopen(r"http://resources.finance.ua/ru/public/currency-cash.json")
    except URLError:
        return "Курс обновляется : УкрСиб"

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    try:
        rate_usd_buy = string_to_float(data['organizations'][10]['currencies']['USD']['bid'])
        rate_usd_sale = string_to_float(data['organizations'][10]['currencies']['USD']['ask'])
        rate_eur_buy = string_to_float(data['organizations'][10]['currencies']['EUR']['bid'])
        rate_eur_sale = string_to_float(data['organizations'][10]['currencies']['EUR']['ask'])
    except IndexError:
        return "Курс уточняется : УкрСиб "

    return "$%s/%s, EUR %s/%s: Агриколь " % (rate_usd_buy, rate_usd_sale, rate_eur_buy, rate_eur_sale)

def nationalBankFinance():
    try:
        resp = urlopen(r"http://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    except URLError:
        return "Курс уточняется : НацБанк"

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    try:
        rate_usd = exchange_validation(string_to_float(data[8]['rate']))
        rate_eur = exchange_validation(string_to_float(data[17]['rate']))
        rate_chf = exchange_validation(string_to_float(data[2]['rate']))
    except IndexError:
        return "Курс уточняется : НацБанк"
    return "$%s, EUR%s, CFH%s : НацБанк У" % (rate_usd, rate_eur, rate_chf)


def string_to_float(s):
    try:
        return round(float(s), 2)
    except ValueError:
        return s

# to open flat files as dictionary
def file_to_dict(file):
    dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            (key, val) = line.split(";")
            dict[key] = int(val)
    return dict

# to open flat files as dictionary
def file_to_dict2(file):

    dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            (key, val) = line.split(";")
            dict[key] = (val)
    return dict


#calculation time beetween to stations for Kiev Metro. a and b - IDs of metro stations
def time_to_station(a,b):
    minV = min(a,b)
    maxV = max(a,b)
    ar1 = [0, 2, 3, 2, 2, 3, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2]
    ar2 = [0, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 4, 3]
    ar3 = [0, 2, 4, 3, 3, 2, 1, 1, 3, 5, 2, 2, 2, 2, 2, 2]
    if minV < 29:
        if maxV < 29: return sum(ar1[minV-10: maxV-10])
        elif 50 < maxV < 69: return sum(ar1[min(minV-10, 11): max(minV-10, 11)]) + sum(ar2[min(maxV-50, 8): max(maxV-50, 8)]) + 3
        elif maxV > 70: return sum(ar1[min(minV-10, 10): max(minV-10, 10)]) + sum(ar3[min(maxV-70, 3): max(maxV-70, 3)]) + 3
    elif minV > 70: return sum(ar3[minV-70: maxV-70])
    elif 50 < minV < 71:
        if maxV < 71: return sum(ar2[minV-50: maxV-50])
        elif maxV > 70: return sum(ar2[min(minV-50, 9): max(minV-50, 9)]) + sum(ar3[min(maxV-70, 3): max(maxV-70, 3)]) + 3
    else: return 0

#to select random value from dictionary
def random_tag():
   dict = file_to_dict2(config.tagOutput)
   rkey = random.choice(list(dict.keys()))
   return dict[rkey]

def random_person_tag():

   dict = file_to_dict2(config.tagOutput)

   keys = list(dict.keys())
   return keys

# need tu be updated
def exchange_validation(s):
    return s

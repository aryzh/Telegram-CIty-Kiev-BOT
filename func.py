# -*- coding: utf-8 -*
# file to store functions for Telegram BOT. For development team only
import random
import codecs
import json
import config
from urllib.request import urlopen, URLError


#функция для парсинга погоды
def weather():
    resp = urlopen(config.weatherURL)
    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    temp_c = data['current_observation']['temp_c']
    status = data['current_observation']['weather']
    humidity = data['current_observation']["relative_humidity"]
    return "Температура в %s сейчас %s C \n %s \n Влажность %s" % ("Киеве", temp_c, status, humidity)

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


def privatBankFinance():
    try:
        resp = urlopen(r"http://resources.finance.ua/ru/public/currency-cash.json")
    except URLError:
        return "Курс уточняется : Приват"
    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    rate_usd_buy = string_to_float(data['organizations'][79]['currencies']['USD']['bid'])
    rate_usd_sale = string_to_float(data['organizations'][79]['currencies']['USD']['ask'])
    rate_eur_buy = string_to_float(data['organizations'][79]['currencies']['EUR']['bid'])
    rate_eur_sale = string_to_float(data['organizations'][79]['currencies']['EUR']['ask'])
    return "$%s/%s, EUR %s/%s: Приват" % (rate_usd_buy, rate_usd_sale, rate_eur_buy, rate_eur_sale)

def UkrSibBankFinance():
    try:
        resp = urlopen(r"http://resources.finance.ua/ru/public/currency-cash.json")
    except URLError:
        return "Курс обновляется : УкрСиб"

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    try:
        rate_usd_buy = string_to_float(data['organizations'][112]['currencies']['USD']['bid'])
        rate_usd_sale = string_to_float(data['organizations'][112]['currencies']['USD']['ask'])
        rate_eur_buy = string_to_float(data['organizations'][112]['currencies']['EUR']['bid'])
        rate_eur_sale = string_to_float(data['organizations'][112]['currencies']['EUR']['ask'])
    except IndexError:
        return "Курс уточняется : УкрСиб"

    return "$%s/%s, EUR %s/%s: УкрСиб" % (rate_usd_buy, rate_usd_sale, rate_eur_buy, rate_eur_sale)

def nationalBankFinance():
    try:
        resp = urlopen(r"http://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    except URLError:
        return "Курс уточняется : НацБанк"

    json_data = resp.read().decode('utf-8', 'replace')
    data = json.loads(json_data)
    try:
        rate_usd = string_to_float(data[54]['rate'])
    except IndexError:
        return "Курс уточняется : НацБанк"
    try:
        rate_eur = string_to_float(data[44]['rate'])
    except IndexError:
        return "Курс уточняется : НацБанк"
    try:
        rate_chf = string_to_float(data[60]['rate'])
    except IndexError:
        return "Курс уточняется : НацБанк"
    return "$%s, EUR%s, CFH%s : НацБанк У" % (rate_usd, rate_usd, rate_chf)


def encodeCustom(s, name, *args, **kwargs):
    codec = codecs.lookup(name)
    rv, length = codec.encode(s, *args, **kwargs)
    if not isinstance(rv, (str, bytes, bytearray)):
        raise TypeError('Not a string or byte codec')
    return rv

def string_to_float(s):
    try:
        return round(float(s), 2)
    except ValueError:
        return s
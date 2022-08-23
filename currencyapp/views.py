from django.shortcuts import render

# Create your views here.
from .models import *
import requests


def ConvertCurrencyFromTo(FromSymbol,ToSymbol,Amount):
    # ConvertCurrencyFromTo("USD", "LBP",1000)
    # for documentation visit : https://exchangerate.host/#/
    #  response  = {"success":true,"query":{"from":"USD","to":"LBP","amount":1000},"info":{"rate":1515.227507},"historical":false,"date":"2022-08-15"
    # ,"result":1515227.507185}
    # response ['success'] = True
    # response ['result'] = 1515227.507185
    # response['info']['rate'] = 1515.227507
    # url = "https://api.exchangerate.host/convert?from=" + FromSymbol + "&to=" + ToSymbol + "&amount=" + str(Amount)
    url = "https://api.exchangerate.host/convert"
    payload = {}
    headers = {}
    parameters = {
                'from' : FromSymbol,
                'to' : ToSymbol,
                'amount' : str(Amount)
               }
    response = requests.request("GET", url, headers=headers, data=payload,params=parameters)
    print(response.text)
    newresponse = json.loads(response.text)
    print(newresponse['success']) # if True means the operation is successful
    print(newresponse['result']) # the amount in the new currency
    print(newresponse['info']['rate']) # the rate of the operation

def GetLatestRate(FromSymbol,ToSymbol):
    # symbols = ["EUR", "LBP", "USD", "SAR", "AED"]
    # GetLatestRate("USD", symbols)
    # for documentation visit : https://exchangerate.host/#/
    #response  = {"success":true,"base":"USD","date":"2022-08-15","rates":{"AED":3.6714,"EUR":0.97524,"LBP":1515.228246,"SAR":3.75399,"USD":1}}
    # response ['success'] = True
    # response ['rates'] = {'AED': 3.6714, 'EUR': 0.97524, 'LBP': 1515.228246, 'SAR': 3.75399, 'USD': 1}
    # response ['rates'][symbols[0]] = 0.97524
    # response ['rates'][symbols[1]] = 1515.228246
    # response ['rates'][symbols[2]] = 1
    # response ['rates'][symbols[3]] = 3.75399
    # response ['rates'][symbols[4]] = 3.6714


    url = "https://api.exchangerate.host/latest"
    payload = {}
    headers = {}
    ToSymbolList =  ','.join(str(e) for e in ToSymbol)
    parameters = {
                'base' : FromSymbol,
                'symbols' : ToSymbolList,
               }
    response = requests.request("GET", url, headers=headers, data=payload,params=parameters)
    print(response.text)
    newresponse = json.loads(response.text)
    print(newresponse['success']) # if True means the operation is successful
    print(newresponse['rates']) # the rates of the operation
    for cur in ToSymbol:
        print(newresponse['rates'][cur])
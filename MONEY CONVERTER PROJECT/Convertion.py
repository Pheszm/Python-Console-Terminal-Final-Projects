import requests
import json
import os
import YouAreLoggedIn
import ConvertionHistoryAdd
from datetime import datetime

def GetExchangeRate(BaseCurrency, TargetCurrency):
    url = f"https://api.exchangerate-api.com/v4/latest/{BaseCurrency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(TargetCurrency)
        return rate
    else:
        raise ValueError("Failed to get the exchange rate.")

def convert_currency(amount, ExchangeRate):
    return amount * ExchangeRate

def Conversions():
    print("\t\t  1. USD")
    print("\t\t  2. PHP")
    print("\t\t  3. EUR")
    Currency = input("\t\t Input Number of the Currency: ")
    if Currency == '1':
        Currency = 'USD'
        
    elif Currency == '2':
        Currency = 'PHP'
        
    elif Currency == '3':
        Currency = 'EUR'
        
    else:
        print("\t\t What you Entered is not in the list")
    return Currency
    
def main(username):
    History = []
    current_date_time = datetime.now()
    History.append(current_date_time.strftime("|%I:%M%p - %Y-%m-%d|"))
    os.system("cls")
    print("\n\t\t      Select a Base Currency")
    BaseCurrency = Conversions()
    History.append(f"{BaseCurrency} = ")
    
    os.system("cls")
    amount = float(input("\n\n\n\t\t Enter Base Currency Amount: "))
    History.append(f"{amount} to ")
    MultiConvert = []
    while True:
        os.system("cls")
        print("\n\t\t      Select Target Currency")
        TargetCurrency = Conversions()

        try:
            ExchangeRate = GetExchangeRate(BaseCurrency, TargetCurrency)
            if ExchangeRate is not None:
                converted_amount = convert_currency(amount, ExchangeRate)
                MultiConvert.append(f"{TargetCurrency}: {converted_amount}")
                History.append(f"{TargetCurrency} ")
                choice = input("\n\t\t Add more Target Currency? (y/n): ")
                if choice == 'y':
                    pass
                else:
                    os.system("cls")
                    print("\n\n\t\tBASE CURRENCY:")
                    print(f"\t\t   {BaseCurrency}: {amount}")
                    print("\n\t\tCONVERTED CURRENCY:")
                    for i in MultiConvert:
                        print("\t\t   ", i)
                    GG = ' '.join(map(str, History))
                    ConvertionHistoryAdd.add(username, GG)

                    input("\n\t\tPRESS ENTER TO GO BACK TO MENU")
                    return YouAreLoggedIn.Logged(username)
            else:
                print("Invalid currencies.")
        except Exception as e:
            print(f"Error: {e}")


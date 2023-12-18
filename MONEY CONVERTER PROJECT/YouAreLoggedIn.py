import time
import os
import csv
import Starter
import msvcrt
import Convertion
import ConvertionHistory

def Logged(username):
    os.system("cls")
    print(f"\n\n\n\t\t     WELCOME TO MONEY CONVERTER {username}!")
    print("\t\t               1. Convert")
    print("\t\t               2. View History")
    print("\t\t               3. Back To Menu")
    
    choice = input("\t\t        Enter Choice(1-3): ")
    if choice == '1':
        Convertion.main(username)
    elif choice == '2':
        ConvertionHistory.List(username)
    elif choice == '3':
        print("\t\t            Going to Menu...")
        time.sleep(2)
        Starter.main()
    else:
        print("\t\t          What you Entered is not in the Choices.")
        time.sleep(2)
        Logged(username)


import os
import Encrypting
import time
import Starter
import csv
import YouAreLoggedIn
import HistoryLoggedIn

def Processing():
    os.system("cls")
    print("\n\n\t\t\t   LOGGING-IN")
    username = input("\t\t\tUserName: ")
    password = Encrypting.EncryptedInput("\t\t\tPassword: ")
    #Encrypting.EncryptedInput
    try:
        with open('AccountData.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

            for row in data:
                if row[0] == username and row[1] == password:
                    print("\n\t                 Login successful!")
                    time.sleep(2)
                    HistoryLoggedIn.AddToHistory(username)
                    YouAreLoggedIn.Logged(username)
                    return None
                    
        print("\n\t\t   Incorrect username or password. Please try again.")
        time.sleep(2)
        return None
        
    except FileNotFoundError:
        print("\n\t\t   Leaderboard file not found. Please check the file name and path.")
        time.sleep(2)
        return None


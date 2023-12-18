import os
import csv
import YouAreLoggedIn

def List(username):
    os.system("cls")
    print("\n\t\t       CONVERSION HISTORY")
    with open('AccountData.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row and row[0] == username:
            history_list = row[2:]
            for history in history_list:
                print(f"\t{history}")
            input("\n\t\t PRESS ENTER TO GO BACK TO MENU")
            YouAreLoggedIn.Logged(username)
            return None

    print(f"\n\t\tUsername '{username}' not found in the list.")
    input("\t\t PRESS ENTER TO GO BACK TO MENU")
    return None



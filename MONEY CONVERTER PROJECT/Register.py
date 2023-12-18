import os
import csv
import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def save_data(self):
        rows = []
        with open('AccountData.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[0] == self.username:
                print("\n\t\t\tCan't Create the Account, Username is Already Used.")
                return False

        empty_row_index = None
        for i, row in enumerate(rows):
            if not any(row):
                empty_row_index = i
                break
        if empty_row_index is not None:
            rows[empty_row_index] = [self.username, self.password]
        else:
            rows.append([self.username, self.password])

        with open('AccountData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return True

def main():
    os.system("cls")
    print("\n\n\t\t\t   Registering Account")
    username = input("\t\t\tEnter a Username: ")
    password = input("\t\t\tEnter a Password: ")

    player = User(username, password)
    if player.save_data():
        print("\n\t\t\tAccount Successfully Created")
    time.sleep(2)
    return None

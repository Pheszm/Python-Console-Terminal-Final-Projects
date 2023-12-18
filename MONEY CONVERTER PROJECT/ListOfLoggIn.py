import csv
import os

def List():
    os.system("cls")
    print("\n\t\t\tHISTORY OF LOGGED-IN USERS")
    
    with open('HistoryOfLoggedIn.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i, row in enumerate(rows[:10], 1):
        # Remove square brackets and format the row content
        formatted_row = ', '.join(row).replace('[', '').replace(']', '')
        print(f"\t\t{i}: {formatted_row}")

    input("\n\t\t\t  PRESS ENTER TO GO BACK")
    return None

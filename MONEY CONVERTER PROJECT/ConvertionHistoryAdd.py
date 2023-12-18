import os
import csv

def add(username, History):
    with open('AccountData.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i, row in enumerate(rows):
        if row and row[0] == username:
            rows[i].append(History) 

    with open('AccountData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return None

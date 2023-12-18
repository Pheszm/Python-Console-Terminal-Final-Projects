import csv
from datetime import datetime

def AddToHistory(username):
    current_date_time = datetime.now()
    CurrentDateTime = current_date_time.strftime("%I:%M%p |%Y-%m-%d|")
    Set = str(f"{username}, Logged-In:{CurrentDateTime}")
    
    with open('HistoryOfLoggedIn.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Insert the new entry at the beginning of the rows list
    rows.insert(0, [Set])

    with open('HistoryOfLoggedIn.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
    return None


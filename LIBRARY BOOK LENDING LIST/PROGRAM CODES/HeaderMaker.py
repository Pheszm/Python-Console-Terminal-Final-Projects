import csv

def SutdentBorrowerHeaderMaker():
    with open('Student Borrower Data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
            
    if not any(rows):
        EmptyRowIndex = None
        for i, row in enumerate(rows):
            if not any(row):
                EmptyRowIndex = i
                break
            
        if EmptyRowIndex is not None:
            rows[EmptyRowIndex] = ["DATE & TIME", "FULL NAME", "STUDENT ID", "BOOK"]
        else:
            rows.append(["DATE & TIME", "FULL NAME", "STUDENT ID", "BOOK"])
            
            
    with open('Student Borrower Data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)  

    return None



def BooksHeaderMaker():
    with open('Book List.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
            
    if not any(rows):
        EmptyRowIndex = None
        for i, row in enumerate(rows):
            if not any(row):
                EmptyRowIndex = i
                break
            
        if EmptyRowIndex is not None:
            rows[EmptyRowIndex] = ["TITLE", "NUMBER OF COPIES", "AVAILABLE"]
        else:
            rows.append(["TITLE", "NUMBER OF COPIES", "AVAILABLE"])
            
            
    with open('Book List.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)  

    return None

import csv
import Color
import Assurance
import msvcrt
import ListOfTheBorrowers
import os
import time

def Remove():
    os.system("cls")
    print("\n\t\t\t\t   ======================================")
    print(f"\t\t\t\t   |{Color.CYAN}     LIST OF THE BOOK BORROWERS     {Color.RESET}|")
    print(f"\t\t\t\t   ======================================")
    
    with open('Student Borrower Data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    with open('Book List.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        Data = list(reader)

    TimeColumn = 0
    NameColumn = 1
    IDColumn = 2
    BooksStartColumns = 3
    numbering = 1
    for row in rows[1:]:
        time = row[TimeColumn]
        name = row[NameColumn]
        student_id = row[IDColumn]
        books_borrowed = ', '.join(filter(None, row[BooksStartColumns:]))  # Remove empty elements
        print(f"\n\t\t\t{Color.CYAN}{numbering}){Color.RESET}")
        print(f"\t\t\tWhen: {time}")
        print(f"\t\t\t{Color.YELLOW}Full-Name: {name}{Color.RESET}")
        print(f"\t\t\t{Color.YELLOW}Student ID: {student_id}{Color.RESET}")
        print(f"\t\t\tBorrowed Book: {books_borrowed}")
        numbering += 1
            
        
    Num = input(f"\n\t\t\t   {Color.CYAN}Which Number from the List you want to Remove: {Color.RESET}")
    GG = len(rows)
    
    try:
        Num = int(Num)
        if Num >= GG or Num < 1:
            print(f"\n\t\t\t\t   {Color.RED} What you Entered is Out of Range.{Color.RESET}")

        elif Assurance.AreYouSure() == True:
            row_number = Num
            BooksInStudent = []

            if row_number <= len(rows):
                row = rows[row_number]
                BooksInStudent = list(row[3:])
                
            
            for i in range (0, len(BooksInStudent)):
                for p in range (0, len(Data)):
                    if BooksInStudent[i] == Data[p][0]:
                        k = int(Data[p][2])
                        k = k+1
                        Data[p][2] = k
                    
            rows.pop(Num)
            print(f"\n\t\t\t    {Color.GREEN}Borrower has been Successfully Removed from the list{Color.RESET}")

            with open('Student Borrower Data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows) 
                
            with open('Book List.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Data)  # Write the updated Data back to the Book List CSV
                
        PressEnterToProceed = msvcrt.getch()
        return None
        
    except ValueError:
        print(f"\n\t\t\t\t   {Color.RED}     Input Only a Number.{Color.RESET}")
        PressEnterToProceed = msvcrt.getch()
        return None

    


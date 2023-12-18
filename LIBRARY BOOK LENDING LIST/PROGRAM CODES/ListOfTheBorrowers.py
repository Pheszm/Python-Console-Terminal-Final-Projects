import msvcrt
import Assurance
import time
import Color
import csv
import os
import MenuOperation
import RemoveABorrower

def ListDown():
    os.system("cls")
    print("\n\t\t\t\t   ======================================")
    print(f"\t\t\t\t   |{Color.CYAN}     LIST OF THE BOOK BORROWERS     {Color.RESET}|")
    print(f"\t\t\t\t   ======================================")
    
    with open('Student Borrower Data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

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
            numbering+=1



    print(f"\n\t\t\t\t    {Color.BLUE}1. Remove A Borrower on the List{Color.RESET}")
    print(f"\t\t\t\t    {Color.RED}2. Go Back To Menu{Color.RESET}")
    Decision = input(f"\t\t\t\t    Enter Your Choice (1-2): ")
    if Decision == '1':
        if Assurance.AreYouSure() == True:
            RemoveABorrower.Remove()
            ListDown()
        else:
            ListDown()
            
    elif Decision == '2':
        if Assurance.AreYouSure() == True:
            MenuOperation.Menu()
        else:
            ListDown()
            
    else: 
        print(f"\n\t\t\t   {Color.RED}What you Entered Is not On the Choices, Please Try Again{Color.RESET}")
        PressEnterToProceed = msvcrt.getch()
        ListDown()
    

import os
import msvcrt
import csv
from datetime import datetime
import Color
import StudentBorrowingBook
import MenuOperation
import HeaderMaker

class Student:
    def __init__(self, FullName, StudentID, WhenBorrowed, Book):
        self.FullName = FullName
        self.StudentID = StudentID
        self.WhenBorrowed = WhenBorrowed
        self.Book = Book

    def AddToList(self):
        Name = self.FullName
        ID = self.StudentID
        Time = self.WhenBorrowed
        Books = self.Book
        
        HeaderMaker.SutdentBorrowerHeaderMaker()
        with open('Student Borrower Data.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        Entry = [Time, Name, ID] + Books

        EmptyRowIndex = None
        for i, row in enumerate(rows):
            if not any(row):
                EmptyRowIndex = i
                break

        if EmptyRowIndex is not None:
            rows[EmptyRowIndex] = Entry
        else:
            rows.append(Entry)

        with open('Student Borrower Data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def InputArea():
    os.system("cls")
    print("\n\n\n\t\t\t\t   ======================================")
    print(f"\t\t\t\t   |       {Color.BLUE} ADD A BOOK BORROWER {Color.RESET}        |")
    print(f"\t\t\t\t   ======================================\n")
    Name = input(f"\t\t\t\t\t{Color.CYAN}Enter Student Full Name: {Color.RESET}")
    ID = input(f"\t\t\t\t\t{Color.YELLOW}Enter Student ID Number: {Color.RESET}")
    if Name and ID: #Proceed if its not Empty
        Time = datetime.now().strftime("%I:%M%p |%Y-%m-%d|")

        print(f"\n\t\t\t\t\t   {Color.GREEN}Press Enter to Proceed.{Color.RESET}") 
        PressEnterToProceed = msvcrt.getch()
        Books = StudentBorrowingBook.GettingTheBooks(Name)

        if len(Books) > 0:
            Set = Student(Name, ID, Time, Books)
            Set.AddToList()
        MenuOperation.Menu()
    print(f"\n\t\t\t\t\t {Color.RED}Cant Proceed if its Empty.{Color.RESET}")
    PressEnterToProceed = msvcrt.getch()
    InputArea() #if one of them is empty then Try again




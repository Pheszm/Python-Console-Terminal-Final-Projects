import csv
import os
import time
import Assurance
import Color
import msvcrt
import SortsData
import ListOfBooksArea

def Add():
    while True:
        os.system("cls")
        print(f"\n\n\t\t\t\t            {Color.BLUE} ADDING A BOOK{Color.RESET}")
        Title = input("\n\t\t\t\t   Book Title: ")
        Copies = input("\t\t\t\t   Number of Copies: ")
        
        try:
            Copies = int(Copies)
            if Copies < 1:
                print(f"\n\t\t\t\t   {Color.RED} Cant Add a Negative Numbers")

            else:
                Available = Copies
                with open('Book List.csv', 'r', newline='') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                EmptyRowIndex = None
                for i, row in enumerate(data):
                    if not any(row):
                        EmptyRowIndex = i
                        break
                
                if EmptyRowIndex is not None:
                    data[EmptyRowIndex] = [Title, Copies, Available]
                else:
                    data.append([Title, Copies, Available])

                with open('Book List.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                    
                print(f"\n\t\t\t\t   {Color.GREEN}SUCCESSFULLY ADDED TO THE LIST")
            PressEnterToProceed = msvcrt.getch()
            return None
        except ValueError:
            print(f"\n\t\t\t\t   {Color.RED}     Input Only a Number.")
            PressEnterToProceed = msvcrt.getch()




def Remove():
    SortsData.SortByTitle()
        
    os.system("cls")   
    print(f"\t\t\t\t            {Color.BLUE} List Of BOOKS {Color.RESET}        ")
    print(f"\t\t\t\t     {Color.CYAN}TITLE {Color.YELLOW}    NO. COPIES{Color.RESET}/{Color.RESET}AVAILABLE{Color.RESET}\n")  
    with open('Book List.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    GG = 0
    
    for i in data:
        GG+=1

    for j in range (1, GG):
        print(f"\t\t\t\t   {Color.GREEN}{j}) {Color.CYAN}{data[j][0]}   {Color.YELLOW}{data[j][1]}{Color.RESET}/{Color.RESET}{data[j][2]}{Color.RESET}")
            
        
    Num = input(f"\n\t\t\t   {Color.CYAN}Which Number from the List you want to Remove: {Color.RESET}")
    GG = len(data)
    
    try:
        Num = int(Num)
        if Num >= GG or Num < 1:
            print(f"\n\t\t\t\t   {Color.RED} What you Entered is Out of Range.{Color.RESET}")

        elif Assurance.AreYouSure() == True:   
            data.pop(Num)
            print(f"\n\t\t\t    {Color.GREEN}The Book has been Successfully Removed from the list{Color.RESET}")

                
            with open('Book List.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data) 
                
        PressEnterToProceed = msvcrt.getch()
        return None
        
    except ValueError:
        print(f"\n\t\t\t\t   {Color.RED}     Input Only a Number.{Color.RESET}")
        PressEnterToProceed = msvcrt.getch()
        return None




def Search():
    os.system("cls")
    print(f"\n\n\t\t\t\t            {Color.BLUE} SEARCHING FOR A BOOK{Color.RESET}")
    title = input("\t\t\t\t\t Enter the book title: ")

    with open('Book List.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    found_books = []
    for row in data[1:]:  # Exclude the header row
        if title.lower() in row[0].lower():  # Case-insensitive search
            found_books.append(row)

    if found_books:
        print("\n\t\t\t  Found Books:")
        for book in found_books:
            print(f"\t\t\t  {Color.CYAN}Title: {book[0]}{Color.RESET},{Color.YELLOW} Copies: {book[1]}{Color.RESET}, Available: {book[2]}")
    else:
        print(f"\t\t\t\t{Color.RED}No books found with the title: {title}{Color.RESET}")
        
    PressEnterToProceed = msvcrt.getch()
    ListOfBooksArea.ListOfBooks()















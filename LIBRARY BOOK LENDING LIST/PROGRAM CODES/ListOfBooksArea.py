import csv
import HeaderMaker
import os
import time
import SortsData
import Assurance
import Color
import msvcrt
import MenuOperation
import BookOperations

def ListOfBooks():
    while True:
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

        print(f"\n\t\t\t\t{Color.BLUE}     1. Add Book{Color.RESET}")
        print(f"\t\t\t\t{Color.BLUE}     2. Remove Book{Color.RESET}")
        print(f"\t\t\t\t{Color.BLUE}     3. Search Book{Color.RESET}")
        print(f"\t\t\t\t{Color.BLUE}     4. Go back to Menu{Color.RESET}") 
        Decision = input("\t\t\t\t     Number of the Book To Add: ")
        if Decision == '1':
            if Assurance.AreYouSure() == True:
                BookOperations.Add()  
            else:
                ListOfBooks()
                
        elif Decision == '2':
            if Assurance.AreYouSure() == True:
                BookOperations.Remove()  
            else:
                ListOfBooks()
                
        elif Decision == '3':
            if Assurance.AreYouSure() == True:
                BookOperations.Search()  
            else:
                ListOfBooks()
                
        elif Decision == '4':
            if Assurance.AreYouSure() == True:
                MenuOperation.Menu()  
            else:
                ListOfBooks()
                
        else:        
            print(f"\n\t\t\t   {Color.RED}What you Entered Is not On the Choices, Please Try Again{Color.RESET}")
            PressEnterToProceed = msvcrt.getch()
            ListOfBooks()





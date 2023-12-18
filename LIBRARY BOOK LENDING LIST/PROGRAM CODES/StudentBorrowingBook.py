import os
import time
import Assurance
import msvcrt
from datetime import datetime
import Color
import BookListToBorrow

def GettingTheBooks(Name):
    Books = []
    while True:
        os.system("cls")
        print(f"\n\t\t\t\t\t {Color.CYAN}{Name}{Color.RESET} Is Borrowing:\n")

        if len(Books) > 0:
            for i in range(0, len(Books)):
                print(f"\t\t\t\t\t{i+1}) {Color.YELLOW}{Books[i]}{Color.RESET}")

        print("\n\t\t\t\t\t1. Add Book")
        print("\t\t\t\t\t2. Finish")        
        Decision = input("\n\t\t\t\t\tEnter Your Choice (1-2): ")
        if Decision == '1':
            if Assurance.AreYouSure() == True:
                ChosenBook = BookListToBorrow.ListOfTheBooks(Books)
                if ChosenBook is not None:
                    Books.append(ChosenBook)
                    
        elif Decision == '2':
            if Assurance.AreYouSure() == True:
                if len(Books) > 0:
                    print(f"\n\t\t\t\t     {Color.GREEN}Student Has been added in the List.{Color.RESET}")
                else:
                    print(f"\n\t\t\t\t     {Color.RED}Student is not added in the List.{Color.RESET}")
                PressEnterToProceed = msvcrt.getch()
                return Books

        else:
            print(f"\n\t\t\t\t   {Color.RED}What you Entered is Not in the Choices{Color.RESET}")
            PressEnterToProceed = msvcrt.getch()

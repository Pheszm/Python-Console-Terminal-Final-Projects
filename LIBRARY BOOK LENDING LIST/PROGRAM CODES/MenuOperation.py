import Assurance
import AddBorrower
import msvcrt
import time
import os
import Color
import ListOfTheBorrowers
import ListOfBooksArea

def Menu():
    os.system("cls")
    print("\n\n\n\t\t\t\t   ======================================")
    print(f"\t\t\t\t   |{Color.BLUE} LOGIN TO BOOK LENDING LIST PROGRAM {Color.RESET}|")
    print(f"\t\t\t\t   ======================================")
    print(f"\t\t\t\t   |{Color.CYAN}                MENU                {Color.RESET}|")
    print(f"\t\t\t\t   |{Color.YELLOW}      1. ADD BORROWER               {Color.RESET}|")
    print(f"\t\t\t\t   |{Color.YELLOW}      2. LIST OF THE BORROWERS      {Color.RESET}|")
    print(f"\t\t\t\t   |{Color.YELLOW}      3. LIST OF THE BOOKS          {Color.RESET}|")
    print(f"\t\t\t\t   |{Color.YELLOW}      4. EXIT                       {Color.RESET}|")
    print(f"\t\t\t\t   ======================================")
    Decision = input("\n\t\t\t\t\tEnter Your Choice (1-4): ")
    
    if Decision == '1':
        if Assurance.AreYouSure() == True:
            AddBorrower.InputArea()
        else:
            Menu()
            
    elif Decision == '2':
        if Assurance.AreYouSure() == True:
           ListOfTheBorrowers.ListDown()
        else:
            Menu()
            
    elif Decision == '3':
        if Assurance.AreYouSure() == True:
           ListOfBooksArea.ListOfBooks()
        else:
            Menu()
        
    elif Decision == '4':
        if Assurance.AreYouSure() == True:
           quit() 
        else:
            Menu()
    else:
        print(f"\n\t\t\t   {Color.RED}What you Entered Is not On the Choices, Please Try Again{Color.RESET}")
        PressEnterToProceed = msvcrt.getch()
        Menu()



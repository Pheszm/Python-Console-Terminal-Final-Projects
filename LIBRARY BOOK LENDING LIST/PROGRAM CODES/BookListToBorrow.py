import csv
import os
import Assurance
import Color
import msvcrt
import SortsData

        
def ListOfTheBooks(Books):
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

        Num = input("\n\t\t\t\t     Number of the Book To Add: ")

        try:
            Num = int(Num)
            if Num >= GG or Num < 0:
                print(f"\n\t\t\t\t   {Color.RED} What you Entered is Out of Range.")
            elif data[Num][0] in Books:
                print(f"\n\t\t\t\t   {Color.RED} Can only get 1 copy of Book")
                PressEnterToProceed = msvcrt.getch()
                return None
            elif int(data[Num][2]) < 1:
                print(f"\n\t\t\t\t  {Color.RED}There is no Available Copy of the Book.")
            elif Assurance.AreYouSure() == True:
                z = int(data[Num][2])
                z = z-1
                data[Num][2] = z
                with open('Book List.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                return str(data[Num][0])
            PressEnterToProceed = msvcrt.getch()
        except ValueError:
            print(f"\n\t\t\t\t   {Color.RED}     Input Only a Number.")
            PressEnterToProceed = msvcrt.getch()


        
    







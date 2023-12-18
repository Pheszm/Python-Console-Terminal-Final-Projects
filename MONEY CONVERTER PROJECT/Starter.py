import msvcrt
import os
import time
import Register
import LoggingIn
import ListOfLoggIn

def main():
    os.system("cls")
    print("\n\n\t\t\t   MONEY CONVERTER")
    print("\t\t\t1) Login")
    print("\t\t\t2) Check Previous Login's")
    print("\t\t\t3) Register")
    print("\t\t\t4) Exit")
    choice = input("\n\t\t        Select Choices(1-4): ")

    if choice == "1":
        LoggingIn.Processing()
            
    elif choice == "2":
        ListOfLoggIn.List()
            
    elif choice == "3":
        Register.main()
        
    elif choice == "4":
        print("\n\t\t\tPress ENTER to EXIT, Press 'Q' if Not")
        Pressed = msvcrt.getch()
        if Pressed == b'\r':
            quit()
        else:
            main()
    else:
        print("\n\t\t  Invalid choice. Please Enter Again.")
        time.sleep(2)
    main()

                
if __name__=="__main__":
    main()

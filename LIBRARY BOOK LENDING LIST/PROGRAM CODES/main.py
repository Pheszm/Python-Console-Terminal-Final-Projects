import MenuOperation
import EncryptTyping
import time
import os
import msvcrt
import Assurance
import Color


class User:
    def __init__(self, Account):
        self.Account = Account

    def GettingAccount(self):
        return self.Account


class Login(User):
    def __init__(self, Account):
        super().__init__(self, Account)

    def LoggingIn(Account):
        print("\n\n\n\t\t\t\t   ======================================")
        print(f"\t\t\t\t   |{Color.BLUE} LOGIN TO BOOK LENDING LIST PROGRAM {Color.RESET}|")
        print(f"\t\t\t\t   ======================================")
        InitialUser = input("\n\t\t\t\t\t\tUser: ")
        InitialPass = EncryptTyping.EncryptedInput("\t\t\t\t\t\tPassword: ")

        for i in range(0, len(Account)-1):
            if InitialUser == Account[i][0]:
                if InitialPass == Account[i][1]:
                    print(f"\n\t\t\t\t\t      {Color.GREEN}You Are Logged In{Color.RESET}")
                    PressEnterToProceed = msvcrt.getch()
                    return True
                
        print(f"\n\t\t\t\t\t   {Color.RED}Wrong User or Password.{Color.RESET}")
        PressEnterToProceed = msvcrt.getch()
        return False


def main():
    os.system("cls")
    Set = User([["Rodelyn", "Jen123"],
                ["Carl", "asd123"],
                ["asdasd", "asdasd"]
                 ])
    
    Acc = Set.GettingAccount()
 
    if Login.LoggingIn(Acc) == True:
        MenuOperation.Menu()

    else:
        print("\n\t\t\t Please Contact the Technical Service for Registering Account")
        PressEnterToProceed = msvcrt.getch()
        main()


if __name__=="__main__":
    main()




    

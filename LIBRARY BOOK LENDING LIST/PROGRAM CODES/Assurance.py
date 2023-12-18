import msvcrt

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = "\033[1m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

def get_char():
    char = msvcrt.getch()
    return char

def AreYouSure():
    Sure = False
    print(f"\n\t\t\t\t   {MAGENTA}Pess Enter if Sure, Backspace if Not.{RESET}")
    KeyPressed = get_char()
    if KeyPressed == b'\r': 
        Sure = True
    else:
        Sure = False

    return Sure



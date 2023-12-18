import msvcrt
import time

def EncryptedInput(prompt):
    print(prompt, end='', flush=True)
    encrypted_input = ''

    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':  # Check for Enter (Carriage Return)
            print()
            break
        elif char == '\x08':  # Check for Backspace
            if encrypted_input:  # Remove last character if there is any
                encrypted_input = encrypted_input[:-1]
                print('\b \b', end='', flush=True)  # Erase the last '*' from the screen
        else:
            encrypted_input += char
            print('*', end='', flush=True)

    return encrypted_input




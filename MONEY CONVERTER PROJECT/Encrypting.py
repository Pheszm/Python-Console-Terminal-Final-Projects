import msvcrt

def EncryptedInput(prompt):
    print(prompt, end='', flush=True)
    encrypted_input = ''

    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':  
            print()
            break
        elif char == '\x08':  
            if encrypted_input:
                encrypted_input = encrypted_input[:-1]
                print('\b \b', end='', flush=True)  
        else:
            encrypted_input += char
            print('*', end='', flush=True)

    return encrypted_input




# 1st python libraries
import os
# 2nd third party libraries
# 3ed custom libraries
from modules.bcolor import Bcolors

def clear():
    """ Clear the console on Windows, MacOS and Linux. """

    # windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    # mac and linux
    else: 
        _ = os.system("clear")

def confirm(msg):
    """ Return True if user write 'yes' or 'y' and False 'no' or 'n' (not sensible). """

    while True:
        userInput = str(input(f"{msg}\n[YES/NO]: {Bcolors.OKGREEN}"))
        print(f"{Bcolors.ENDC}")

        if userInput.lower() in ('y', 'yes'):
            return True
        elif userInput.lower() in ('n', 'no'):
            return False
        else:
            print_error("Ustede no ingresó una opción válida, por favor vuelva a intentarlo.")
            continue

def delete_file(path):
    """ Delete a file in a path. Acepts one String argument with the absolute path. """

    if os.path.exists(path):
        try:
            os.remove(path)
            return True
        except:
            print_error("No se pudo borrar el archivo por algún error desconocido.")
    else:
        print_error("El archivo que intenta borrar no existe.")
    
    return False

def print_error(msg):
    """ Print with style an error messagge. """

    print(f"\n{Bcolors.CREDBG}  {msg}  {Bcolors.ENDC}")
    input(f"{Bcolors.FAIL}-> Presiona ENTER para continuar{Bcolors.ENDC}\n")
    clear()
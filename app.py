# 1st python libraries
# import datetime as dt

# 2nd third party libraries
import pandas as pd

# 3ed custom libraries
from modules.functions import clear, confirm, delete_file, print_error
from modules.bcolor import Bcolors

# run when this file is executed as main (python app.py)
if __name__ == "__main__":
    clear()

    DATABASE_PATH = "dist/database.csv"

    name = input("Name: ")
    surname = input("Hola meté tu apellido: ")
    email = input("Email: ")

    data = {
        "Name": [name, "Nacho", "Franco", "Leo", "Ari"],
        "Surname": [surname, "Spera", "Venini", "Banche", "Pont"],
        "Email": [email, "nacho@gmail.com", "franco@gmail.com", "banche@gmail.com", "ari@gmail.com"]
    }

    # Create a dataframe
    df = pd.DataFrame(data, columns = ["Name", "Surname", "Email"])

    # Create the .csv file
    try:
        df.to_csv(DATABASE_PATH)
    except PermissionError:
        print_error("El archivo está abierto en otro programa, por favor cerrarlo y volver a intentar.")

    # Update the .csv file
    new_data = {'Email': ["arielpont41@gmail.com"]}
    new_df = pd.DataFrame(new_data, index = [4])
    
    try:
        df.update(new_df)
    except PermissionError:
        print_error("El archivo está abierto en otro programa, por favor cerrarlo y volver a intentar.")

    # Read and print the new dataframe updated
    clear()
    df2 =  pd.read_csv(DATABASE_PATH)
    print(f"{Bcolors.HEADER}{df2}{Bcolors.ENDC}")

    # Delete
    if confirm("¿Desea borrar la base de datos?"):
        delete_file(DATABASE_PATH)
    else:
        print(f"{Bcolors.OKGREEN}La base de datos se ha conservado{Bcolors.ENDC}")

    # menu options
    options = [
        "Show values",
        "Show Top 10 values",
        # "Exit" must be always the last option
        "Exit"
    ]

    # menu
    while True:
        print("Welcome! Select an option please:\n")

        # check if options is not empety and a LIST or a TUPLE
        if options != "" and type(options) is list or type(options) is tuple:
            
            # print options
            count = 1
            for option in options:
                print(f"{str(count)}. {option}")
                count += 1

            # input an option
            while True:
                try:
                    userInput = int(input(f"\nSelect an option: "))      
                except ValueError:
                    print("Please, write a valid option number between 1 and {len(options)}")
                    continue
                else:
                    if(userInput > len(options) or userInput == 0):
                        print(f"Please, write a valid option number between 1 and {len(options)}.")
                        continue
                    break

            if(userInput == len(options)):
                print("Bye!")
                exit
            else:
                clear()
                print(f"You selected the option: {options[userInput-1]}")
                continue

        else:
            raise TypeError("Menu need a <list> or <tuple> to show options")
        break

# imports
try:
    import datetime as dt
except ImportError:
    print("ImportError: <dt>.")
    dt = None

try:
    import os
except ImportError:
    print("ImportError: <os>.")
    os = None

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("ImportError: <plt>.")
    plt = None

try:
    from matplotlib import style
except ImportError:
    print("ImportError: <style>.")
    style = None

try:
    import pandas as pd
except ImportError:
    print("ImportError: <pd>.")
    pd = None

try:
    import pandas_datareader.data as web
except ImportError:
    print("ImportError: <web>.")
    web = None

# functions
def clear(): 
    # windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    # mac and linux
    else: 
        _ = os.system("clear")

# run when this file is executed as main (python app.py)
if __name__ == "__main__":
    clear()

    # menu options
    options = (
        "Show values",
        "Show Top 10 values",
        # "Exit" must be always the last option
        "Exit"
    )

    # menu
    while True:
        print("Welcome! Select an option please:\n")

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

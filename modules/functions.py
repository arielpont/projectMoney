# 1st python libraries
import os
# 2nd custom libraries
# 3ed third party libraries

def clear(): 
    # windows 
    if os.name == "nt": 
        _ = os.system("cls") 
    # mac and linux
    else: 
        _ = os.system("clear")
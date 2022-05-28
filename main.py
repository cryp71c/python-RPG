import sys
import json
import os
import pandas as pd
import hashlib
from IPython.display import display
import __main__
import socket

###########################################################################
## Will need to implement load/save files for Windows 10+ and poss linux ##
###########################################################################
number = 0

##### TEST DATA ############################################################################################################
test_data = {'Save': number, 'Character': 'Harry', 'Level': 1, 'EXP': 0, 'Gold': 0, 'hp': 100, 'mp': 100, 'atk': 10,       #
             'defn': 10, 'matk': 10, 'mdef': 10, 'spd': 10, 'luck': 10}                                                    #
test_data = pd.DataFrame(test_data, index=[0])                                                                             #
############################################################################################################################
def check_file_integrity():
    current_running_file = str(__main__.__file__) # Check name of current running file
    BUF_SIZE= 65536 # Set Buffer Size
    md5 = hashlib.md5() # Set MD5 Object
    sha1 = hashlib.sha1() # Set SHA1 Object
    
    with open(current_running_file, 'rb') as f: # Open and read current file.
        while True:
            data = f.read(BUF_SIZE) # Read defined Buffer Size 
            if not data:
                break
            md5.update(data) # Update the MD5 Hash
            sha1.update(data) # Update the SHA1 Hash

    HOST = '127.0.0.1' # Certification Server address
    PORT = 44556 # Certification Port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create clients socket

    s.connect((HOST,PORT)) # Connect to Certification Server 127.0.0.1:44556

    hash = s.recv(32).decode('utf-8') # Recive true hash from Certification Serve

    if hash != md5.hexdigest(): # Check for hashing mismatch
        print("[!] HASH MISMATCH QUITTING DUE TO FILE INTEGRITY.") # Print out file mismatch error
        print(f"Current: {md5.hexdigest()} -- Server Response: {hash}") # Print out both hashes. Upload to virustotal.com to check for malware
        quit() # Quit
    else:
        if debug == True: # Debug setting for debug checking.
            print("[*] File Integrity : OK")

    s.close()
    return()

def load_data(file): # Loads Saved Game Data
    load = pd.DataFrame()
    ## Depending on OS FS Structure
    path = os.getcwd() + '/' + file + ".json"

    print(path)
    
    l = open(path,'r')

    j_file = json.load(l)

    df = pd.json_normalize(j_file)

    return(df)

def save_data(df): # Saves Game Data
    global number
    number += 1
    save_name = input("What would you like to name your save file? ")
    path = os.getcwd()
    if len(save_name) > 10:
        save_name = f"save_{number}.json"
    else:
        save_name = save_name + ".json"

    path = path + "/" + save_name ## Fix with os checking eventually to support win/unix

    s = open(path, 'w')

    df['Save'] = save_name
    df['save_path'] = path
    s.write(df.to_json(orient='records'))
    s.close()

    print("Game Saved!")

def display_title():
    print("    Celestial Adventurer") # Title and Save Selection.
    print("\t1: New Game")
    print("\t2: Load Game")
    print("\t3: Save Game")
    print("\t4: Quit Game")    

def game_menu():
    pass

def game_menu_selection():
    pass

def main():
    global debug # Debug access variable
    debug = False
    args = sys.argv[1:]
    if "d" in args[0]:
        debug = True
    if "i" in args[0]:
        check_file_integrity()
    game = True
    title = True
    while game:
        try:
            if debug == True:
                print("[*] Game Running Entering Title Screen")
            while title:
                display_title()
                if debug == True:
                    print("[*] Displaying Title")
                try:
                    if debug == True:
                        print("[*] Asking for user selection")
                    menu_selection = int(input("    >"))
                    if menu_selection not in [1,2,3,4]:
                        if debug == True:
                            print(f"[*] User selection is {menu_selection}")
                        print("Invalid Menu Selection.")
                        main()
                    if menu_selection == 1:
                        if debug == True:
                            print("[*] User selected New Game")
                        print("New Game")
                    if menu_selection == 2:
                        if debug == True:
                            print("[*] User selected Load Game")
                        print("Load Game")
                    if menu_selection == 3:
                        if debug == True:
                            print("[*] User selected Save Game")
                        print("Save Game")
                    if menu_selection == 4:
                        if debug == True:
                            print("[*] Quitting")
                        quit()

                except ValueError:
                    if debug == True:
                        print(f"[*] User has Value Error. Re-running Main.")
                    print("Invalid Menu Selection.")                        
                    main()
                title = False

            game = False
        except KeyboardInterrupt as kerr:
            if debug == True:
                print(f"Keyboard Interrupt {err=}")
            print("User interrupted game.")
            quit()
        
        # menu_select = select_menu_item()
        # game_menu()

    #save_data(test_data)
    #load_data(input("File Name to Load: "))

if __name__ == "__main__":
    main()
from distutils.log import debug
import json
import os
from re import A
from tkinter import E
from turtle import title
from numpy import char
import pandas as pd
from IPython.display import display

### Implement os checking and file saving mechanics.
#print(os.name)

number = 0

test_data = {'Save': number, 'Character': 'Harry', 'Level': 1, 'EXP': 0, 'Gold': 0, 'hp': 100, 'mp': 100, 'atk': 10,
             'defn': 10, 'matk': 10, 'mdef': 10, 'spd': 10, 'luck': 10}
test_data = pd.DataFrame(test_data, index=[0])

def load_data(file):
    load = pd.DataFrame()
    ## Depending on OS FS Structure
    path = os.getcwd() + '/' + file + ".json"

    print(path)
    
    l = open(path,'r')

    j_file = json.load(l)

    df = pd.json_normalize(j_file)

    return(df)

def save_data(df):
    global number
    number += 1
    save_name = input("What would you like to name your save file? ")
    path = os.getcwd()
    if len(save_name) > 10:
        save_name = f"save_{number}.json"
    else:
        save_name = save_name + ".json"

    path = path + "/" + save_name ## Fix with os checking eventually to support win/unix

    #print(path)

    s = open(path, 'w')

    df['Save'] = save_name
    df['save_path'] = path
    s.write(df.to_json(orient='records'))
    s.close()

    print("Game Saved!")

def display_title():
    print("    Celestial Adventurer")
    print("\t1: New Game")
    print("\t2: Load Game")
    print("\t3: Save Game")
    print("\t4: Quit Game")    

def game_menu():
    pass

def game_menu_selection():
    pass

#display(test_data.to_json(orient='records'))

def main():
    debug = True
    game = True
    title = True
    while game:
        try:
            #os.system('cls || clear || clr || cl || c')
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
            #os.system('cls || clear || clr || cl || c')
            quit()
        
        # menu_select = select_menu_item()
        # game_menu()



    #save_data(test_data)
    #load_data(input("File Name to Load: "))

if __name__ == "__main__":
    main()
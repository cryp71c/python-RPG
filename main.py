import json
import os
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

def select_menu_item(menu_item):
    pass

def game_menu():
    pass

def game_menu_selection():
    pass

#display(test_data.to_json(orient='records'))

game = True

while game:
    os.system('cls || clear || clr || cl || c')
    display_title()
    game = False
    # menu_select = select_menu_item()
    # game_menu()



#save_data(test_data)
#load_data(input("File Name to Load: "))
import json

import pandas as pd
from IPython.display import display

number = 0

test_data = {'Save': number, 'Character': 'Harry', 'Level': 1, 'EXP': 0, 'Gold': 0, 'hp': 100, 'mp': 100, 'atk': 10,
             'defn': 10, 'matk': 10, 'mdef': 10, 'spd': 10, 'luck': 10}
test_data = pd.DataFrame(test_data, index=[0])


def save_data(df):
    global number
    number += 1

    save_name = input("What would you like to name your save file? ")
    if len(save_name) > 10:
        save_name = f"save_{number}.json"
    else:
        save_name = save_name + ".json"

    s = open(save_name, 'w')

    df['Save'] = save_name
    s.write(df.to_json(orient='records'))
    s.close()


display(test_data.to_json(orient='records'))

save_data(test_data)

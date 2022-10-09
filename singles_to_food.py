#!/usr/bin/env python3

import json
import pprint


# tuneables
food_file = "food.json"
single_file = "single.json"

# globals
food = {}
single = {}

pp = pprint.PrettyPrinter(indent=4)


def load_food_file():
    global food
    with open(food_file, 'r') as file:
        food = json.load(file)


def load_single_file():
    global single
    with open(single_file, 'r') as file:
        single = json.load(file)


def write_food_file():
    with open(food_file, 'w') as file:
        json.dump(food, file)




### MAIN ###
load_food_file()
load_single_file()

for s in single.keys():
    food[s] = single[s]  
    print(f"food: {s}")
    pp.pprint(food[s])
    print()

# write_food_file()

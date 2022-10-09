#!/usr/bin/env python3

# TODO recipes encapsulate items

import json


# tuneables
food_file = "food.json"

# globals
food = {}


def load_food_file():
    global food
    # with open('https://site/food.json', 'r') as file:
    with open(food_file, 'r') as file:
        food = json.load(file)


### MAIN ###
load_food_file()

# minimum servings logic here
for k in food.keys():
    kcal = food[k]['kcal'] + 0
    carb = food[k]['carb'] + 0
    fat = food[k]['fat'] + 0
    protein = food[k]['protein'] + 0
    sodium = food[k]['sodium'] + 0

    tkcal = carb * 4 + fat * 9 + protein * 4
    # if tkcal == kcal:
    #     print("%-33s tkcal %4d==kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
    #           (k, tkcal, kcal, carb, fat, protein, sodium))
    if tkcal != kcal:
        print("%-33s tkcal %4d!=kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
              (k, tkcal, kcal, carb, fat, protein, sodium))

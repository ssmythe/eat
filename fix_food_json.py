#!/usr/bin/env python3

import json

food_file = "food.json"

# globals
food = {}


def load_food_file():
    global food
    with open(food_file, 'r') as file:
        food = json.load(file)


def write_food_file():
    global food
    with open(food_file, 'w') as file:
        json.dump(food, file)


def fix_kcal():
    global food
    for k in food.keys():
        kcal = food[k]['kcal'] + 0
        carb = food[k]['carb'] + 0
        fat = food[k]['fat'] + 0
        protein = food[k]['protein'] + 0
        sodium = food[k]['sodium'] + 0

        food[k]['kcal'] = carb * 4 + fat * 9 + protein * 4


load_food_file()
fix_kcal()
write_food_file()

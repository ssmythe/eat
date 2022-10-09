#!/usr/bin/env python3

# TODO recipes encapsulate items

import random
import json


# tuneables
calc_menus = 7
min_kcal = 1600
max_kcal = 1638
min_sodium = 500
max_sodium = 2000
food_file = "food.json"

# globals
food = {}
keys_params = ['kcal', 'carb', 'fat', 'protein', 'sodium']
max_params = {}
min_params = {}
total = {}
shopping = {}
count = 0


def load_food_file():
    global food
    # with open('https://site/food.json', 'r') as file:
    with open(food_file, 'r') as file:
        food = json.load(file)

def calculate_kcal():
    global food
    for k in food.keys():
        food[k]['kcal'] = 0
        carb = food[k]['carb'] + 0
        fat = food[k]['fat'] + 0
        protein = food[k]['protein'] + 0
        sodium = food[k]['sodium'] + 0
        food[k]['kcal'] = carb * 4 + fat * 9 + protein * 4


def init_total_params():
    total['kcal'] = 0
    total['carb'] = 0
    total['fat'] = 0
    total['protein'] = 0
    total['sodium'] = 0


def init_params():
    max_params['kcal'] = max_kcal
    max_params['carb'] = max_params['kcal'] * 0.5 / 4
    max_params['fat'] = max_params['kcal'] * 0.3 / 9
    max_params['protein'] = max_params['kcal'] * 0.2 / 4
    max_params['sodium'] = max_sodium

    min_params['kcal'] = min_kcal
    min_params['carb'] = min_params['kcal'] * 0.5 / 4
    min_params['fat'] = min_params['kcal'] * 0.3 / 9
    min_params['protein'] = min_params['kcal'] * 0.2 / 4
    min_params['sodium'] = min_sodium

    init_total_params()


def break_check():
    for k in keys_params:
        if total[k] + kcal > max_params[k]:
            break


def init_menu_key():
    if not k in menu.keys():
        menu[k] = 0


def inc_menu_key():
    if k in menu.keys():
        menu[k] = menu[k] + 1
    else:
        menu[k] = 1


def inc_shopping_keys():
    for k in menu.keys():
        if k in shopping.keys():
            shopping[k] = shopping[k] + menu[k]
        else:
            shopping[k] = menu[k]


def params_under_max():
    rc = True
    for k in keys_params:
        if total[k] > max_params[k]:
            rc = False
    return rc


def params_in_min_max_window():
    rc = True
    for k in keys_params:
        if total[k] < min_params[k] or total[k] > max_params[k]:
            rc = False
    return rc


### MAIN ###
load_food_file()
calculate_kcal()
init_params()

for i in range(1, calc_menus + 1):
    while True:
        menu = {}
        init_total_params()

        # minimum servings logic here
        for k in food.keys():
            min_servings = food[k]['min_servings']
            if min_servings > 0:
                kcal = food[k]['kcal'] * min_servings
                carb = food[k]['carb'] * min_servings
                fat = food[k]['fat'] * min_servings
                protein = food[k]['protein'] * min_servings
                sodium = food[k]['sodium'] * min_servings
                max_servings = food[k]['max_servings']
                menu[k] = min_servings

        while params_under_max():
            k = random.choice(list(food.keys()))
            kcal = food[k]['kcal']
            carb = food[k]['carb']
            fat = food[k]['fat']
            protein = food[k]['protein']
            sodium = food[k]['sodium']
            max_servings = food[k]['max_servings']

            if max_servings == 0:
                continue

            if k in menu.keys():
                if menu[k] == max_servings:
                    continue

            break_check()

            total['kcal'] = total['kcal'] + kcal
            total['carb'] = total['carb'] + carb
            total['fat'] = total['fat'] + fat
            total['protein'] = total['protein'] + protein
            total['sodium'] = total['sodium'] + sodium

            inc_menu_key()

            if params_in_min_max_window():
                break

        if params_in_min_max_window():
            break

        count = count + 1
        # print(count, end='\r')

    print(f"Menu #{i}: {count} runs")
    print("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
          ("Totals:", total['kcal'], total['carb'], total['fat'], total['protein'], total['sodium']))
    print("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
          ("Maxs:", max_params['kcal'], max_params['carb'], max_params['fat'], max_params['protein'], max_params['sodium']))
    print(90 * '-')
    for k in sorted(menu.keys()):
        servings = menu[k]
        kcal = food[k]['kcal'] * servings
        carb = food[k]['carb'] * servings
        fat = food[k]['fat'] * servings
        protein = food[k]['protein'] * servings
        sodium = food[k]['sodium'] * servings
        print("%dx %-30s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
                (servings, k, kcal, carb, fat, protein, sodium))
    print(90 * '-')
    for k in sorted(menu.keys()):
        servings = menu[k]
        kcal = food[k]['kcal']
        carb = food[k]['carb']
        fat = food[k]['fat']
        protein = food[k]['protein']
        sodium = food[k]['sodium']
        for i in range(1, servings + 1):
            print("[ ] %s" % (k))


    inc_shopping_keys()
    print()

# Shopping List
print()
print(f"Shopping List:")
print()
for k in sorted(shopping.keys()):
    servings = shopping[k]
    kcal = food[k]['kcal'] * servings
    carb = food[k]['carb'] * servings
    fat = food[k]['fat'] * servings
    protein = food[k]['protein'] * servings
    sodium = food[k]['sodium'] * servings
    check_boxes = servings * "[ ]"
    print("%2dx %-30s  %s" % (servings, k, check_boxes))

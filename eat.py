#!/usr/bin/env python3

# TODO read food from file
# TODO read food from URL
# TODO command line interface for number of menus to produce

import random


food = {
    'almond milk': {'kcal': 30, 'carb': 1, 'fat': 2.5, 'protein': 1, 'sodium': 0, 'max_servings': 999},
    'honeycrisp apple': {'kcal': 80, 'carb': 22, 'fat': 0, 'protein': 0, 'sodium': 0, 'max_servings': 999},
    'protein powder 0.5': {'kcal': 60, 'carb': 2, 'fat': 1, 'protein': 12, 'sodium': 53, 'max_servings': 999},
    'salad with anlvr dressing': {'kcal': 72, 'carb': 10, 'fat': 3, 'protein': 2, 'sodium': 73, 'max_servings': 2},
    'special k and almond milk': {'kcal': 157, 'carb': 28, 'fat': 4, 'protein': 3, 'sodium': 356, 'max_servings': 999},
    'toast with hummus': {'kcal': 150, 'carb': 19, 'fat': 6, 'protein': 7, 'sodium': 200, 'max_servings': 999},
    'tofurky chao mayo sandwich': {'kcal': 389, 'carb': 39, 'fat': 17, 'protein': 28, 'sodium': 777, 'max_servings': 999},
    'yellow peach': {'kcal': 60, 'carb': 15, 'fat': 0, 'protein': 1, 'sodium': 0, 'max_servings': 999},
    'yukon gold potato': {'kcal': 110, 'carb': 52, 'fat': 0, 'protein': 6, 'sodium': 0, 'max_servings': 999},
}

# tuneables
min_pct = 0.90
max_kcal = 2000
min_sodium = 500
max_sodium = 2000

# globals
keys_params = ['kcal', 'carb', 'fat', 'protein', 'sodium']
max_params = {}
min_params = {}
total = {}
count = 0


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

    min_params['kcal'] = max_kcal * min_pct
    min_params['carb'] = min_params['kcal'] * 0.5 / 4
    min_params['fat'] = min_params['kcal'] * 0.3 / 9
    min_params['protein'] = min_params['kcal'] * 0.2 / 4
    min_params['sodium'] = min_sodium

    init_total_params()


def break_check():
    for k in keys_params:
        if total[k] + kcal > max_params[k]:
            break


def inc_menu_key():
    if k in menu.keys():
        menu[k] = menu[k] + 1
    else:
        menu[k] = 1


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
init_params()

while True:
    menu = {}
    init_total_params()

    while params_under_max():
        k = random.choice(list(food.keys()))
        kcal = food[k]['kcal']
        carb = food[k]['carb']
        fat = food[k]['fat']
        protein = food[k]['protein']
        sodium = food[k]['sodium']
        max_servings = food[k]['max_servings']

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
    print(count, end='\r')


print(f"Menu: {count} runs")
print("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
      ("Totals:", total['kcal'], total['carb'], total['fat'], total['protein'], total['sodium']))
print("%-33s kcal %4d, carb %4d, fat %3d, protein %3d, sodium %4d" %
      ("Maxs:", max_params['kcal'], max_params['kcal'], max_params['fat'], max_params['protein'], max_params['sodium']))
print(88 * '-')
for k in sorted(menu.keys()):
    servings = menu[k]
    kcal = food[k]['kcal'] * servings
    carb = food[k]['carb'] * servings
    fat = food[k]['fat'] * servings
    protein = food[k]['protein'] * servings
    sodium = food[k]['sodium'] * servings
    check_boxes = servings * "[ ]"
    print("%dx %-30s kcal %4d, carb %3d, fat %3d, protein %3d, sodium %4d  %s" %
          (servings, k, kcal, carb, fat, protein, sodium, check_boxes))

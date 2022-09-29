#!/usr/bin/env python3

# TODO refactor globals for min and max values into data structure to iterate
# TODO refactor break logic state into functions
# TODO read food from file
# TODO read food from URL
# TODO command line interface for number of menus to produce

import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

min_pct = 0.90

max_kcal = 2000
min_kcal = max_kcal * min_pct
total_kcal = 0
max_carb = max_kcal * 0.5 / 4
min_carb = max_carb *min_pct
total_carb = 0
max_fat = max_kcal * 0.3 / 9
min_fat = max_fat * min_pct
total_fat = 0
max_protein = max_kcal * 0.2 / 4
min_protein = max_protein * min_pct
total_protein = 0
max_sodium = 2000
total_sodium = 0
count = 0

food = {
    'almond milk': { 'kcal': 30, 'carb': 1, 'fat': 2.5, 'protein': 1, 'sodium': 0, 'max_servings': 999 } ,
    'honeycrisp apple': { 'kcal': 80, 'carb': 22, 'fat': 0, 'protein': 0, 'sodium': 0, 'max_servings': 999 } ,
    'protein powder 0.5': { 'kcal': 60, 'carb': 2, 'fat': 1, 'protein': 12, 'sodium': 53, 'max_servings': 999 } ,
    'salad with anlvr dressing': { 'kcal': 72, 'carb': 10, 'fat': 3, 'protein': 2, 'sodium': 73, 'max_servings': 2 },
    'special k and almond milk': { 'kcal': 157, 'carb': 28, 'fat': 4, 'protein': 3, 'sodium': 356, 'max_servings': 999 },
    'toast with hummus': { 'kcal': 150, 'carb': 19, 'fat': 6, 'protein': 7, 'sodium': 200, 'max_servings': 999 }, 
    'tofurky chao mayo sandwich': { 'kcal': 389, 'carb': 39, 'fat': 17, 'protein': 28, 'sodium': 777, 'max_servings': 999 }, 
    'yellow peach': { 'kcal': 60, 'carb': 15, 'fat': 0, 'protein': 1, 'sodium': 0, 'max_servings': 999 } ,
    'yukon gold potato': { 'kcal': 110, 'carb': 52, 'fat': 0, 'protein': 6, 'sodium': 0, 'max_servings': 999 } ,
}

while True:
    menu = {}
    total_kcal = 0
    total_carb = 0
    total_fat = 0
    total_protein = 0
    total_sodium = 0

    while total_kcal <= max_kcal and total_carb <= max_carb and total_fat <= max_fat and total_protein <= max_protein and total_sodium <= max_sodium:
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

        if total_kcal + kcal > max_kcal:
            break
        if total_carb + carb > max_carb:
            break
        if total_fat + fat > max_fat:
            break
        if total_protein + protein > max_protein:
            break
        if total_sodium + kcal > max_sodium:
            break
        
        total_kcal = total_kcal + kcal
        total_carb = total_carb + carb
        total_fat = total_fat + fat
        total_protein = total_protein + protein
        total_sodium = total_sodium + sodium

        if k in menu.keys():
            menu[k] = menu[k] + 1
        else:
            menu[k] = 1

        if total_kcal >= min_kcal and total_carb >= min_carb and total_fat >= min_fat and total_protein >= min_protein and total_kcal <= max_kcal and total_carb <= max_carb and total_fat <= max_fat and total_protein <= max_protein and total_sodium <= max_sodium:
            break

    if total_kcal >= min_kcal and total_carb >= min_carb and total_fat >= min_fat and total_protein >= min_protein and total_kcal <= max_kcal and total_carb <= max_carb and total_fat <= max_fat and total_protein <= max_protein and total_sodium <= max_sodium:
        break

    count = count + 1
    print(count, end='\r')


print(f"Menu: {count} runs")
print("%-33s kcal %4d, carb %3d, fat %3d, protein %3d, sodium %4d" % ("Totals:", total_kcal, total_carb, total_fat, total_protein, total_sodium))
print("%-33s kcal %4d, carb %3d, fat %3d, protein %3d, sodium %4d" % ("Maxs:", max_kcal, max_carb, max_fat, max_protein, max_sodium))
print(88 * '-')
for k in sorted(menu.keys()):
    servings = menu[k]
    kcal = food[k]['kcal'] * servings
    carb = food[k]['carb'] * servings
    fat = food[k]['fat'] * servings
    protein = food[k]['protein'] * servings
    sodium = food[k]['sodium'] * servings
    check_boxes = servings * "[ ]"
    print("%dx %-30s kcal %4d, carb %3d, fat %3d, protein %3d, sodium %4d  %s" % (servings, k, kcal, carb, fat, protein, sodium, check_boxes))

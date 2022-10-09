#!/usr/bin/env python3

import json
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

food_file = "food.json"


def write_food_file():
    with open(food_file, 'w') as file:
        json.dump(food, file)


def load_food_file():
    # with open('https://e6v4p8w2.rocketcdn.me/Users/nikpi/Desktop/iss-now.json', 'r') as file:
    with open(food_file, 'r') as file:
        food = json.load(file)


# DEBUG: remove exit for first time run
print("WARNING: please remove exit() the first time you run this!!!")
exit(1)

write_food_file()
load_food_file()

print(food)

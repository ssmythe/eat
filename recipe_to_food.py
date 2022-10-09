#!/usr/bin/env python3

import json
import pprint


# tuneables
food_file = "food.json"
ingredient_file = "ingredient.json"
recipe_file = "recipe.json"

# globals
food = {}
ingredient = {}
recipe = {}

pp = pprint.PrettyPrinter(indent=4)


def load_food_file():
    global food
    with open(food_file, 'r') as file:
        food = json.load(file)


def load_ingredient_file():
    global ingredient
    with open(ingredient_file, 'r') as file:
        ingredient = json.load(file)


def load_recipe_file():
    global recipe
    with open(recipe_file, 'r') as file:
        recipe = json.load(file)


def write_food_file():
    with open(food_file, 'w') as file:
        json.dump(food, file)


def add_food_key(name, key, value):
    global food

    # print(f"Adding {name}: key={key}, value={value}")

    if not name in food.keys():
        food[name] = {}

    if key in food[name].keys():
        food[name][key] = food[name][key] + value
    else:
        food[name][key] = value


### MAIN ###
load_food_file()
load_ingredient_file()
load_recipe_file()

for r in recipe.keys():
    # print(f"recipe: {r}")
    # pp.pprint(recipe[r])
    servings = recipe[r]['servings']
    serving_size = recipe[r]['serving size']
    min_servings = recipe[r]['min_servings']
    max_servings = recipe[r]['max_servings']

    add_food_key(r, 'serving_size', serving_size)
    add_food_key(r, 'servings per container', servings)
    add_food_key(r, 'store', 'recipe')
    add_food_key(r, 'store product name', 'recipe')
    add_food_key(r, 'min_servings', min_servings)
    add_food_key(r, 'max_servings', max_servings)

    for i in recipe[r]['ingredients'].keys():
        # print(f"ingredient: {i}")
        # pp.pprint(ingredient[i])
        iqty = recipe[r]['ingredients'][i]
        ispc = ingredient[i]['servings per container']
        carb = ingredient[i]['carb'] * iqty / servings
        fat = ingredient[i]['fat'] * iqty / servings
        protein = ingredient[i]['protein'] * iqty / servings
        sodium = ingredient[i]['sodium'] * iqty / servings
        price = round(ingredient[i]['price'] * iqty / ispc / servings, 2)

        add_food_key(r, 'carb', carb)
        add_food_key(r, 'fat', fat)
        add_food_key(r, 'protein', protein)
        add_food_key(r, 'sodium', sodium)
        add_food_key(r, 'price', price)

        # print(f"food: {r}")
        # pp.pprint(food[r])
        # print()

write_food_file()

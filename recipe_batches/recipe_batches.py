#!/usr/bin/python

import math

recipe_test = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredients_test = {'milk': 198, 'butter': 52, 'cheese': 10}


def recipe_batches(recipe, ingredients):
    recipe_item = list(recipe.keys())
    ingredients_items = list(ingredients.keys())
    smallest_possible = ingredients[ingredients_items[0]] // recipe[recipe_item[0]]
    print(recipe[recipe_item[0]])
    print(smallest_possible)
    if len(recipe) != len(ingredients):
        return 0

    for i in ingredients:
        if ingredients[ingredients_items[i]] // recipe[recipe_item[i]] < smallest_possible:
            smallest_possible = ingredients[ingredients_items[i]] // recipe[recipe_item[i]]
            return smallest_possible



recipe_batches(recipe_test, ingredients_test)
# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

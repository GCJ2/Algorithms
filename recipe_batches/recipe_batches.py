#!/usr/bin/python

import math

recipe_test = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredients_test = {'milk': 198, 'butter': 52, 'cheese': 10}


def recipe_batches(recipe, ingredients):
    # put each item from recipe into a list by key
    recipe_item = list(recipe.keys())
    # put each item from ingredient into a list by key
    # Can't seem to iterate through a dictionary the same way as a list
    # So pull out the values into a list
    ingredients_items = list(ingredients.keys())
    # Find possible smallest by dividing ingredients by what the recipe calls for
    # Round that number down
    smallest_possible = ingredients[ingredients_items[0]] // recipe[recipe_item[0]]
    # If the length of the recipe is longer than the length of the ingredients
    # We know we don't have everything and can return 0
    if len(recipe) > len(ingredients):
        return 0

    for i in ingredients:
        # Smallest possible is already set to the first recipe item // first ingredient
        # If ing // rec is smaller than current smallest possible
        if ingredients[i] // recipe[i] < smallest_possible:
            # Set smallest possible to that new value
            smallest_possible = ingredients[i] // recipe[i]
            return smallest_possible
        else:
            return smallest_possible


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

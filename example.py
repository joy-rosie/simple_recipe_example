from typing import List, Dict


class Ingredient:
    def __init__(self, name: str, quantityUnit: str):
        # TODO: we should be using an id
        self.name = name
        # TODO: units should be their own class
        self.quantityUnit = quantityUnit


class Recipe:
    def __init__(self, name: str, ingredients: Dict[Ingredient, float]):
        self.name = name
        self.ingredients = ingredients


def get_total_ingredients(recipes: List[Recipe]) -> Dict[Ingredient, float]:
    total_ingredients = {}
    for recipe in recipes:
        for ingredient, amount in recipe.ingredients.items():
            if ingredient not in total_ingredients:
                total_ingredients[ingredient] = 0
            total_ingredients[ingredient] += amount
    return total_ingredients


def print_ingredients(ingredients: Dict[Ingredient, float]) -> None:
    for ingredient, amount in sorted(ingredients.items(), key=lambda t: t[0].name):
        print(ingredient.name + ": " + str(amount) + ingredient.quantityUnit)


yeast = Ingredient("Yeast", "g")
salt = Ingredient("Salt", "g")
water = Ingredient("Water", "ml")
flour = Ingredient("Flour", "g")


# Not actual recipes!
pizza_dough = Recipe(
    "Pizza Dough",
    {
        yeast: 1,
        salt: 10,
        water: 500,
        flour: 500
    }
)
bread_dough = Recipe(
    "Bread dough",
    {
        yeast: 5,
        salt: 20,
        water: 500,
        flour: 800
    }
)


print_ingredients(get_total_ingredients([
    pizza_dough,
    bread_dough
]))



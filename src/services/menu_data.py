# Req 3
from src.models.dish import Dish, Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, 'r') as file:
            results = csv.DictReader(file)
            dishes = {}
            for row in results:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])
                if dish not in dishes:
                    dishes[dish] = Dish(dish, price)
                dishes[dish].add_ingredient_dependency(Ingredient(ingredient),
                                                       recipe_amount)
                self.dishes = set(dishes.values())

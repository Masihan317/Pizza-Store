from ingredient import Ingredient
import csv

class IngredientRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_ingredients(self, ingredients: list[Ingredient]):
    with open(self.__filename, "w", newline="") as file:
      writer = csv.writer(file)
      for ingredient in ingredients:
        writer.writerow(ingredient.to_list())

  def load_ingredients(self) -> list[Ingredient]:
    with open(self.__filename, newline="") as file:
      reader = csv.reader(file)
      ingredients = []
      for row in reader:
        ingredient = Ingredient(row[0], int(row[1]), int(row[2]), row[3])
        ingredients.append(ingredient)
    return ingredients
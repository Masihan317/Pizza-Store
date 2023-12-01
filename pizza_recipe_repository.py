from pizza_recipe import PizzaRecipe
import csv

class PizzaRecipeRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_pizza_recipes(self, recipes: list[PizzaRecipe]):
    with open(self.__filename, "w", newline="") as file:
      writer = csv.writer(file)
      for recipe in recipes:
        writer.writerow(recipe.to_list())

  def load_pizza_recipes(self) -> list[PizzaRecipe]:
    with open(self.__filename, newline="") as file:
      reader = csv.reader(file)
      recipes = []
      for row in reader:
        ingredients = {}
        for i in range(2, len(row), 2):
          ingredients[row[i]] = row[i + 1]
        recipe = PizzaRecipe(row[0], ingredients, float(row[1]))
        recipes.append(recipe)
    return recipes
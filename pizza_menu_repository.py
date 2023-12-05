from pizza_menu_item import PizzaMenuItem
from recipe_manager import *
import csv

class PizzaMenuRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_pizza_menu(self, recipes: list[PizzaMenuItem]) -> None:
    with open(self.__filename, "w", newline="") as file:
      writer = csv.writer(file)
      for recipe in recipes:
        writer.writerow(recipe.to_list())

  def load_pizza_menu(self) -> list[PizzaMenuItem]:
    with open(self.__filename, newline="") as file:
      reader = csv.reader(file)
      recipe_manager = RecipeManager()
      recipe_manager.read_from_file()
      menu_items = []
      for row in reader:
        recipe = recipe_manager.get_recipe_by_name(row[4])
        menu_item = PizzaMenuItem(row[0], row[1], float(row[2]), row[3], recipe, row[5])
        menu_items.append(menu_item)
    return menu_items
from ingredient import Ingredient
from ingredient_repository import IngredientRepository

class InventoryManager:
  def __init__(self) -> None:
    self.__ingredients: list[Ingredient] = []

  def add_ingredient(self, ingredient: Ingredient):
    existing = False
    for existing_ingredient in self.__ingredients:
      if existing_ingredient.name == ingredient.name:
        existing_ingredient.quantity += ingredient.quantity
        existing = True
    if not existing:
      self.__ingredients.append(ingredient)

  def remove_ingredient(self, name: str, quantity: int):
    for ingredient in self.__ingredients:
      if ingredient.name == name:
        ingredient.quantity -= quantity
        self.check_reorder_levels()

  def use_ingredient(self, recipe: dict[str, int]):
    for ingredient, quantity in recipe:
      self.remove_ingredient(ingredient, quantity)
      self.check_reorder_levels()

  def check_reorder_levels(self):
    for ingredient in self.__ingredients:
      if ingredient.quantity < ingredient.reorder_level:
        print(f"Alert! The supply of {ingredient.name} is low. Please add more.\n")

  def print_inventory(self):
    for ingredient in self.__ingredients:
      print(ingredient)
      print()

  def save_to_file(self) -> None:
    repository = IngredientRepository("ingredients.csv")
    repository.save_ingredients(self.__ingredients)

  def read_from_file(self) -> None:
    repository = IngredientRepository("ingredients.csv")
    self.__ingredients = repository.load_ingredients()
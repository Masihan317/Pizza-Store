from pizza_recipe import PizzaRecipe
from pizza_recipe_repository import PizzaRecipeRepository

class RecipeManager:
  def __init__(self) -> None:
    self.__recipes: list[PizzaRecipe] = []

  def add_recipe(self, recipe: PizzaRecipe):
    self.__recipes.append(recipe)

  def remove_recipe(self, recipe_name: str):
    for recipe in self.__recipes:
      if recipe.name == recipe_name:
        self.__recipes.remove(recipe)

  def update_recipe(self, recipe_name: str, new_ingredients: dict[str, int]):
    for recipe in self.__recipes:
      if recipe.name == recipe_name:
        recipe.ingredients = new_ingredients

  def get_recipe_by_name(self, recipe_name: str) -> PizzaRecipe:
    for recipe in self.__recipes:
      if recipe.name == recipe_name:
        return recipe

  def list_recipes(self):
    for recipe in self.__recipes:
      print(recipe)

  def save_to_file(self) -> None:
    repository = PizzaRecipeRepository("pizza_recipes.csv")
    repository.save_pizza_recipes(self.__recipes)

  def read_from_file(self) -> None:
    repository = PizzaRecipeRepository("pizza_recipes.csv")
    self.__recipes = repository.load_pizza_recipes()
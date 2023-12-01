from inventory_manager import *
from recipe_manager import *
from side_dish_manager import *
from order_manager import *

class PizzaStore:
  def __init__(self) -> None:
    self.__inventory_manager = InventoryManager()
    self.__recipe_manager = RecipeManager()
    self.__side_dish_manager = SideDishManager()
    self.__order_manager = OrderManager()
    self.__inventory_manager.read_from_file()
    self.__recipe_manager.read_from_file()
    self.__side_dish_manager.read_from_file()

  def show_main_menu(self):
    print("Welcome to the Pizza Store Application!")
    print("Pizza Store Menu (Please enter a number from 1 to 5.)")
    print("1. Recipe Manager System")
    print("2. Ingredient Inventory System")
    print("3. Side Dish Manager System")
    print("4. Order Manager System")
    print("5. Quit")

  def show_recipe_menu(self):
    print("Welcome to the Recipe Manager System!")
    print("Recipe Manager Menu (Please enter a number from 1 to 6.)")
    print("1. Add Recipe")
    print("2. Remove Recipe")
    print("3. Update Recipe")
    print("4. Search Recipe")
    print("5. List Recipes")
    print("6. Return to Pizza Store Application")

  def show_inventory_menu(self):
    print("Welcome to the Ingredient Inventory System!")
    print("Ingredient Inventory Menu (Please enter a number from 1 to 5.)")
    print("1. Add Ingredient")
    print("2. Remove Ingredient")
    print("3. Check Ingredient Supply")
    print("4. List Ingredients")
    print("5. Return to Pizza Store Application")

  def show_side_dish_menu(self):
    print("Welcome to the Side Dish Manager System!")
    print("Side Dish Manager Menu (Please enter a number from 1 to 6.)")
    print("1. Add Side Dish")
    print("2. Remove Side Dish")
    print("3. Search Side Dish by Name")
    print("4. List Side Dishes by Type")
    print("5. List All Side Dishes")
    print("6. Return to Pizza Store Application")

  def show_order_menu(self):
    print("Welcome to the Order Manager System!")

  def process_main_menu(self, option: int) -> bool:
    if option == 1:
      flag = True
      while flag:
        self.show_recipe_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_recipe_menu(option)
    elif option == 2:
      flag = True
      while flag:
        self.show_inventory_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_inventory_menu(option)
    elif option == 3:
      flag = True
      while flag:
        self.show_side_dish_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_side_dish_menu(option)
    elif option == 4:
      flag = True
      while flag:
        self.show_order_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_order_menu(option)
    elif option == 5:
      print("Thank you for using the Pizza Store Application! I hope it helped :D")
      return False
    return True

  def process_recipe_menu(self, option: int) -> bool:
    if option == 1:
      recipe_name = input("Please enter the name of the recipe: ")
      price = float(input("Please enter the name of an ingredient: "))
      flag = True
      ingredients = {}
      while flag:
        ingredient = input("Please enter the name of an ingredient: ")
        quantity = int(input("Please enter the quantity of that ingredient: "))
        ingredients[ingredient] = quantity
        confirmation = input("Are there any more ingredients to add? (y/n) ")
        if confirmation.lower() == "y":
          flag = True
        else:
          flag = False
      recipe = PizzaRecipe(recipe_name, ingredients, price)
      self.__recipe_manager.add_recipe(recipe)
    elif option == 2:
      recipe_name = input("Please enter the name of the recipe: ")
      self.__recipe_manager.remove_recipe(recipe_name)
    elif option == 3:
      recipe_name = input("Please enter the name of the recipe to change: ")
      flag = True
      new_ingredients = {}
      while flag:
        ingredient = input("Please enter the name of new ingredient: ")
        quantity = int(input("Please enter the quantity of that new ingredient: "))
        new_ingredients[ingredient] = quantity
        confirmation = input("Are there any more ingredients to add? (y/n) ")
        if confirmation.lower() == "y":
          flag = True
        else:
          flag = False
      self.__recipe_manager.update_recipe(recipe_name, new_ingredients)
    elif option == 4:
      recipe_name = input("Please enter the name of the recipe: ")
      print()
      recipe = self.__recipe_manager.get_recipe_by_name(recipe_name)
      print(recipe)
    elif option == 5:
      print("Here is the list of recipes in the system.\n")
      self.__recipe_manager.list_recipes()
    elif option == 6:
      print("Returning to Pizza Store Application...")
      self.__recipe_manager.save_to_file()
      return False
    return True

  def process_inventory_menu(self, option: int) -> bool:
    if option == 1:
      ingredient_name = input("Please enter the name of the ingredient: ")
      quantity = int(input("Please enter the quantity of the ingredient: "))
      reorder_level = int(input("Please enter the reorder level of the ingredient: "))
      ingredient = Ingredient(ingredient_name, quantity, reorder_level)
      self.__inventory_manager.add_ingredient(ingredient)
    elif option == 2:
      ingredient_name = input("Please enter the name of the ingredient: ")
      quantity = int(input("Please enter the quantity of the ingredient: "))
      self.__inventory_manager.remove_ingredient(ingredient_name, quantity)
    elif option == 3:
      self.__inventory_manager.check_reorder_levels()
    elif option == 4:
      self.__inventory_manager.print_inventory()
    elif option == 5:
      self.__inventory_manager.save_to_file()
      return False
    return True

  def process_side_dish_menu(self, option: int) -> bool:
    if option == 1:
      side_dish_name = input("Please enter the name of the side dish: ")
      description = input("Please enter the description of the side dish: ")
      price = float(input("Please enter the price of the side dish: "))
      type = input("Please enter the type of the side dish: ")
      side_dish = SideDish(side_dish_name, description, price, type)
      self.__side_dish_manager.add_side_dishes(side_dish)
    elif option == 2:
      side_dish_name = input("Please enter the name of the side dish to remove: ")
      self.__side_dish_manager.remove_side_dishes(side_dish_name)
    elif option == 3:
      side_dish_name = input("Please enter the name of the side dish: ")
      self.__side_dish_manager.get_side_dishes_by_name(side_dish_name)
    elif option == 4:
      side_dish_type = input("Please enter the type of the side dish: ")
      self.__side_dish_manager.get_side_dishes_by_type(side_dish_type)
    elif option == 5:
      self.__side_dish_manager.list_side_dishes()
    elif option == 6:
      self.__side_dish_manager.save_to_file()
      return False
    return True

  def process_order_menu(self, option: int) -> bool:
    pass

def main():
  app = PizzaStore()
  flag = True
  while flag:
    app.show_main_menu()
    option = int(input("Enter your choice: "))
    print()
    flag = app.process_main_menu(option)
    print()

if __name__ == "__main__":
  main()
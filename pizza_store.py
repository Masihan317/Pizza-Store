from inventory_manager import *
from recipe_manager import *
from pizza_menu_manager import *
from side_dish_manager import *
from order_manager import *
from custom_pizza_item import *

class PizzaStore:
  def __init__(self) -> None:
    self.__inventory_manager = InventoryManager()
    self.__recipe_manager = RecipeManager()
    self.__pizza_menu_manager = PizzaMenuManager()
    self.__side_dish_manager = SideDishManager()
    self.__order_manager = OrderManager()
    self.__inventory_manager.read_from_file()
    self.__recipe_manager.read_from_file()
    self.__pizza_menu_manager.read_from_file()
    self.__side_dish_manager.read_from_file()
    self.__order_manager.read_from_file()

  def show_main_menu(self) -> None:
    print("Welcome to the Pizza Store Application!")
    print("Pizza Store Menu (Please enter a number from 1 to 5.)")
    print("1. Recipe Manager System")
    print("2. Ingredient Inventory System")
    print("3. Pizza Menu Manager System")
    print("4. Side Dish Menu Manager System")
    print("5. Order Manager System")
    print("6. Quit")

  def show_recipe_menu(self) -> None:
    print("Welcome to the Recipe Manager System!")
    print("Recipe Manager Menu (Please enter a number from 1 to 6.)")
    print("1. Add Recipe")
    print("2. Remove Recipe")
    print("3. Update Recipe")
    print("4. Search Recipe")
    print("5. List Recipes")
    print("6. Return to Pizza Store Application")

  def show_inventory_menu(self) -> None:
    print("Welcome to the Ingredient Inventory System!")
    print("Ingredient Inventory Menu (Please enter a number from 1 to 5.)")
    print("1. Add Ingredient")
    print("2. Remove Ingredient")
    print("3. Check Ingredient Supply")
    print("4. List Ingredients")
    print("5. Return to Pizza Store Application")

  def show_menu_item_menu(self) -> None:
    print("Welcome to the Pizza Menu Manager System! (Please enter a number from 1 to 7.)")
    print("1. Add Pizza Menu Item")
    print("2. Remove Pizza Menu Item")
    print("3. Update Pizza Menu Item")
    print("4. Search Pizza Menu Item by Name")
    print("5. Get Pizza Menu Item by Category")
    print("6. List All Pizza Menu Item")
    print("7. List Custom Pizza Item Options")
    print("8. Return to Pizza Store Application")

  def show_side_dish_menu(self) -> None:
    print("Welcome to the Side Dish Manager System!")
    print("Side Dish Manager Menu (Please enter a number from 1 to 6.)")
    print("1. Add Side Dish")
    print("2. Remove Side Dish")
    print("3. Search Side Dish by Name")
    print("4. Get Side Dishes by Type")
    print("5. List All Side Dishes")
    print("6. Return to Pizza Store Application")

  def show_order_menu(self):
    print("Welcome to the Order Manager System! (Please enter a number from 1 to 11.)")
    print("1. Add Order")
    print("2. Remove Order")
    print("3. Process Order")
    print("4. Process All Orders")
    print("5. Display Order Detail")
    print("6. Display Order Details for All Orders")
    print("7. Generate Order Slips for Kitchen")
    print("8. Generate All Order Slips for Kitchen")
    print("9. Print Customer Receipt")
    print("10. Print All Receipts")
    print("11. Return to Pizza Store Application")

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
        self.show_menu_item_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_menu_item_menu(option)
    elif option == 4:
      flag = True
      while flag:
        self.show_side_dish_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_side_dish_menu(option)
    elif option == 5:
      flag = True
      while flag:
        self.show_order_menu()
        option = int(input("Enter your choice: "))
        print()
        flag = self.process_order_menu(option)
    elif option == 6:
      print("Thank you for using the Pizza Store Application! I hope it helped :D")
      return False
    return True

  def process_recipe_menu(self, option: int) -> bool:
    if option == 1:
      recipe_name = input("Please enter the name of the recipe: ")
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
      recipe = PizzaRecipe(recipe_name, ingredients)
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
      unit = input("Please enter the unit of the ingredient: ")
      ingredient = Ingredient(ingredient_name, quantity, reorder_level, unit)
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
      print("Returning to Pizza Store Application...")
      self.__inventory_manager.save_to_file()
      return False
    return True

  def process_menu_item_menu(self, option: int) -> bool:
    if option == 1:
      name = input("Please enter the name of the menu item: ")
      description = input("Please enter the description of the menu item: ")
      price = float(input("Please enter the price of the menu item: "))
      size = input("Please enter the size of the menu item (SMALL/MEDIUM/LARGE): ")
      recipe_name = input("Please enter the recipe name of the menu item: ")
      recipe = self.__recipe_manager.get_recipe_by_name(recipe_name)
      category = input("Please enter the category of the menu item (VEGETARIAN/MEATLOVERS/SPECIALTY): ")
      menu_item = PizzaMenuItem(name, description, price, size, recipe, category)
      self.__pizza_menu_manager.add_menu_item(menu_item)
    elif option == 2:
      name = input("Please enter the name of the menu item to remove: ")
      self.__pizza_menu_manager.remove_menu_item(name)
    elif option == 3:
      name = input("Please enter the name of the menu item: ")
      description = input("Please enter the new description of the menu item: ")
      price = float(input("Please enter the new price of the menu item: "))
      size = input("Please enter the new size of the menu item (SMALL/MEDIUM/LARGE): ")
      recipe_name = input("Please enter the new recipe name of the menu item: ")
      recipe = self.__recipe_manager.get_recipe_by_name(recipe_name)
      category = input("Please enter the new category of the menu item (VEGETARIAN/MEATLOVERS/SPECIALTY): ")
      menu_item = PizzaMenuItem(name, description, price, size, recipe, category)
      self.__pizza_menu_manager.update_menu_item(name, menu_item)
    elif option == 4:
      name = input("Please enter the name of the menu item: ")
      menu_item = self.__pizza_menu_manager.get_menu_items_by_name(name)
      print(menu_item)
    elif option == 5:
      category = input("Please enter the category of the menu item (VEGETARIAN/MEATLOVERS/SPECIALTY): ")
      menu_items = self.__pizza_menu_manager.get_menu_items_by_category(category)
      for menu_item in menu_items:
        print(menu_items)
        print()
    elif option == 6:
      menu_items = self.__pizza_menu_manager.list_menu_items()
    elif option == 7:
      self.print_custom_pizza_info()
    elif option == 8:
      print("Returning to Pizza Store Application...")
      self.__pizza_menu_manager.save_to_file()
      return False
    return True

  def process_side_dish_menu(self, option: int) -> bool:
    if option == 1:
      side_dish_name = input("Please enter the name of the side dish: ")
      description = input("Please enter the description of the side dish: ")
      price = float(input("Please enter the price of the side dish: "))
      type = input("Please enter the type of the side dish (APPETIZER/DESSERT/BEVERAGE): ")
      side_dish = SideDish(side_dish_name, description, price, type)
      self.__side_dish_manager.add_side_dish(side_dish)
    elif option == 2:
      side_dish_name = input("Please enter the name of the side dish to remove: ")
      self.__side_dish_manager.remove_side_dish(side_dish_name)
    elif option == 3:
      side_dish_name = input("Please enter the name of the side dish: ")
      self.__side_dish_manager.get_side_dish_by_name(side_dish_name)
    elif option == 4:
      side_dish_type = input("Please enter the type of the side dish (APPETIZER/DESSERT/BEVERAGE): ")
      self.__side_dish_manager.get_side_dishes_by_type(side_dish_type)
    elif option == 5:
      self.__side_dish_manager.list_side_dishes()
    elif option == 6:
      self.__side_dish_manager.save_to_file()
      return False
    return True

  def process_order_menu(self, option: int) -> bool:
    if option == 1:
      customer_name = input("Please enter the customer name: ")
      customer_phone = input("Please enter the customer phone: ")
      customer_email = input("Please enter the customer email: ")
      standard_pizzas = []
      while True:
        add_std_pizza = input("Are there any more standard pizza orders to add? (y/n) ").lower()
        if add_std_pizza == 'n':
          break
        name = input("Please enter the name of the standard pizza item: ")
        size = input("Please enter the size of the standard pizza item (SMALL/MEDIUM/LARGE): ")
        standard_pizza = self.__pizza_menu_manager.get_menu_items_by_name(name, size)
        standard_pizzas.append(standard_pizza)
      custom_pizzas = []
      while True:
        add_cust_pizza = input("Are there any more custom pizza orders to add? (y/n) ").lower()
        if add_cust_pizza == 'n':
          break
        size = input("Please enter the size of the custom pizza item (SMALL/MEDIUM/LARGE): ")
        crust = input("Please enter the crust of the custom pizza item (ORIGINAL/THIN/GLUTEN_FREE): ")
        sauce = input("Please enter the sauce of the custom pizza item (MARINARA/BBQ_SAUCE/ALFREDO_SAUCE): ")
        ingredients = {}
        while True:
          ingredient = input("Please enter the name of a custom ingredient: ")
          quantity = int(input("Please enter the quantity of that ingredient: "))
          ingredients[ingredient] = quantity
          more_ingredients = input("Are there any more ingredients to add? (y/n) ").lower()
          if more_ingredients == 'n':
            break
        custom_pizza = CustomPizzaItem(size, crust, sauce, ingredients)
        custom_pizzas.append(custom_pizza)
      side_dishes = []
      while True:
        add_side_dish = input("Are there any more side dish orders to add? (y/n) ").lower()
        if add_side_dish == 'n':
          break
        name = input("Please enter the name of the side dish item: ")
        side_dish = self.__side_dish_manager.get_side_dish_by_name(name)
        side_dishes.append(side_dish)
        order = Order(customer_name, customer_phone, customer_email, standard_pizzas, custom_pizzas, side_dishes)
        self.__order_manager.add_order(order)
    elif option == 2:
      order_num = int(input("Please enter the order number: "))
      self.__order_manager.remove_order(order_num)
    elif option == 3:
      order_num = int(input("Please enter the order number: "))
      order = self.__order_manager.search_order(order_num)
      processed = self.__order_manager.check_order_status(order_num)
      if not processed:
        for standard_pizza in order.standard_pizzas:
          self.__inventory_manager.use_ingredient(standard_pizza.recipe.ingredients)
        for custom_pizza in order.custom_pizzas:
          self.__inventory_manager.use_ingredient(custom_pizza.ingredients)
        self.__inventory_manager.save_to_file()
        self.__order_manager.process_order(order_num)
    elif option == 4:
      orders = self.__order_manager.list_orders()
      not_processed = self.__order_manager.check_all_orders_status()
      for order in orders:
        if order.order_num in not_processed:
          for standard_pizza in order.standard_pizzas:
            self.__inventory_manager.use_ingredient(standard_pizza.recipe.ingredients)
          for custom_pizza in order.custom_pizzas:
            self.__inventory_manager.use_ingredient(custom_pizza.ingredients)
      self.__inventory_manager.save_to_file()
      self.__order_manager.process_all_orders()
    elif option == 5:
      order_num = int(input("Please enter the order number: "))
      order = self.__order_manager.search_order(order_num)
      print(order)
      print()
    elif option == 6:
      orders = self.__order_manager.list_orders()
      print("\n\n".join(order.__str__() for order in orders))
      print()
    elif option == 7:
      order_num = int(input("Please enter the order number: "))
      print(self.__order_manager.generate_order_slips_for_kitchen(order_num))
      print()
    elif option == 8:
      orders = self.__order_manager.generate_all_order_slips_for_kitchen()
      print("\n\n".join(orders))
      print()
    elif option == 9:
      order_num = int(input("Please enter the order number: "))
      print(self.__order_manager.generate_receipt_for_customer(order_num))
      print()
    elif option == 10:
      orders = self.__order_manager.generate_all_receipts()
      print("\n\n".join(orders))
      print()
    elif option == 11:
      self.__order_manager.save_to_file()
      return False
    return True

  def print_custom_pizza_info(self):
    custom_pizza_info = "There's an option to create your own pizza.\n"
    custom_pizza_info += "Please pick a size:\n"
    custom_pizza_info += " | ".join([size.name for size in CustomPizzaSize])
    custom_pizza_info += "\nPlease pick a crust:\n"
    custom_pizza_info += " | ".join([crust.name for crust in CustomPizzaCrust])
    custom_pizza_info += "\nPlease pick a sauce:\n"
    custom_pizza_info += " | ".join([sauce.name for sauce in CustomPizzaSauce])
    custom_pizza_info += "\nPlease pick your toppings:\n"
    custom_pizza_info += f"{self.__inventory_manager.list_available_ingredients()}\n"
    print(custom_pizza_info)

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
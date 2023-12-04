from order import Order
from side_dish_manager import *
from pizza_menu_manager import *
from custom_pizza_item import *
import json

class OrderRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_orders(self, orders: list[Order]):
    lst = []
    for order in orders:
      order_object = {
        "name": order.name,
        "phone": order.phone,
        "email": order.email,
        "standard_pizza": [],
        "custom_pizza": [],
        "side_dish": [],
        "processed": order.processed
      }
      for standard_pizza in order.standard_pizzas:
        order_object["standard_pizza"].append({"name": standard_pizza.name, "size": standard_pizza.size})
      for custom_pizza in order.custom_pizzas:
        order_object["custom_pizza"].append({"size": custom_pizza.size, "crust": custom_pizza.crust, "sauce": custom_pizza.sauce, "ingredients": custom_pizza.ingredients})
      for side_dish in order.side_dishes:
        order_object["side_dish"].append(side_dish.name)
      lst.append(order_object)

    json_object = json.dumps({"orders": lst}, indent=2)
    with open(self.__filename, "w") as file:
      file.write(json_object)

  def load_orders(self):
    with open(self.__filename) as file:
      data = json.load(file)

      side_dish_manager = SideDishManager()
      side_dish_manager.read_from_file()
      pizza_menu_manager = PizzaMenuManager()
      pizza_menu_manager.read_from_file()

      orders = []
      orders_data = data["orders"]
      for order_data in orders_data:
        name = order_data.get("name")
        phone = order_data.get("phone")
        email = order_data.get("email")

        pizzas = []
        pizza_names = order_data.get("standard_pizza")
        if pizza_names is not None:
          for pizza_data in pizza_names:
            pizza_name = pizza_data.get("name")
            pizza_size = pizza_data.get("size")
            pizza = pizza_menu_manager.get_menu_items_by_name(pizza_name, pizza_size)
            pizzas.append(pizza)

        custom_pizzas = []
        custom_pizza_data = order_data.get("custom_pizza")
        if custom_pizza_data is not None:
          for cpd in custom_pizza_data:
            custom_pizza_size = cpd.get("size")
            custom_pizza_crust = cpd.get("crust")
            custom_pizza_sauce = cpd.get("sauce")
            custom_pizza_ingredients = cpd.get("ingredients")
            custom_pizza = CustomPizzaItem(custom_pizza_size, custom_pizza_crust, custom_pizza_sauce, custom_pizza_ingredients)
            custom_pizzas.append(custom_pizza)

        side_dishes = []
        side_dishes_names = order_data.get("side_dish")
        if side_dishes_names is not None:
          for side_dish_name in side_dishes_names:
            side_dish = side_dish_manager.get_side_dish_by_name(side_dish_name)
            side_dishes.append(side_dish)

        processed = order_data.get("processed")
        if processed is None:
          processed = False

        order = Order(name, phone, email, pizzas, custom_pizzas, side_dishes, processed)
        orders.append(order)
    return orders
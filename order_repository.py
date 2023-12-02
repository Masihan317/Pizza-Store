from order import Order
import json

class OrderRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_orders(self, orders: list[Order]):
    pass

  def load_orders(self):
    with open(self.__filename) as file:
      data = json.load(file)
      orders = []
      orders_data = data["orders"]
      for order_data in orders_data:
        name = order_data.get("name")
        phone = order_data.get("phone")
        email = order_data.get("email")
        standard_pizza = order_data.get("standard_pizza")
        custom_pizza = order_data.get("custom_pizza")
        side_dish = order_data.get("side_dish")
        order = Order(name, phone, email, standard_pizza, custom_pizza, side_dish)
        orders.append(order)
    for order in orders:
      print(order)
    return orders

repo = OrderRepository("orders.json")
repo.load_orders()

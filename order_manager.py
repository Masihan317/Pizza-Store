from order import *
from order_repository import OrderRepository

class OrderManager:
  def __init__(self) -> None:
    self.__orders: list[Order] = []

  def add_order(self, order: Order):
    self.__orders.append(order)

  def remove_order(self, order_num: int):
    for order in self.__orders:
      if order.order_num == order_num:
        self.__orders.remove(order)

  def process_order(self, order_num):
    for order in self.__orders:
      if order.order_num == order_num:
        order.processed = True

  def process_all_orders(self):
    for order in self.__orders:
      order.processed = True

  def display_order_detail(self, order_num: int):
    for order in self.__orders:
      if order.order_num == order_num:
        return order.__str__()

  def display_all_orders_detail(self):
    order_details = []
    for order in self.__orders:
      order_details.append(order.__str__())
    return order_details

  def generate_order_slips_for_kitchen(self, order_num: int):
    for order in self.__orders:
      if order.order_num == order_num:
        return order.kitchen_slip()

  def generate_all_order_slips_for_kitchen(self):
    order_slips = []
    for order in self.__orders:
      order_slips.append(order.kitchen_slip())
    return order_slips

  def generate_receipt_for_customer(self, order_num: int) -> str:
    for order in self.__orders:
      if order.order_num == order_num:
        return order.receipt()

  def generate_all_receipts(self) -> list[str]:
    receipts = []
    for order in self.__orders:
      receipts.append(order.receipt())
    return receipts

  def save_to_file(self) -> None:
    repository = OrderRepository("orders.json")
    repository.save_orders(self.__orders)

  def read_from_file(self) -> None:
    repository = OrderRepository("orders.json")
    self.__orders = repository.load_orders()
from order import *
from order_repository import OrderRepository

class OrderManager:
  def __init__(self) -> None:
    self.__orders: list[Order] = []

  def add_order(self, order: Order) -> None:
    self.__orders.append(order)

  def remove_order(self, order_num: int) -> None:
    for order in self.__orders:
      if order.order_num == order_num:
        self.__orders.remove(order)

  def search_order(self, order_num: int) -> Order:
    for order in self.__orders:
      if order.order_num == order_num:
        return order

  def list_orders(self) -> list[Order]:
    orders = []
    for order in self.__orders:
      orders.append(order)
    return orders

  def check_order_status(self, order_num: int) -> bool:
    for order in self.__orders:
      if order.order_num == order_num:
        return order.processed

  def check_all_orders_status(self) -> list[int]:
    processed = []
    for order in self.__orders:
      if not order.processed:
        processed.append(order.order_num)
    return processed

  def process_order(self, order_num: int) -> None:
    for order in self.__orders:
      if order.order_num == order_num:
        order.processed = True

  def process_all_orders(self) -> None:
    for order in self.__orders:
      order.processed = True

  def generate_order_slips_for_kitchen(self, order_num: int) -> str:
    for order in self.__orders:
      if order.order_num == order_num:
        return order.kitchen_slip()

  def generate_all_order_slips_for_kitchen(self) -> list[str]:
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
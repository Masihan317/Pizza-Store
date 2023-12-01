class Order:
  no_of_orders = 0

  def __init__(self) -> None:
    Order.no_of_orders += 1
    self.__order_id = Order.no_of_orders
    
class Order:
  no_of_orders = 0

  def __init__(self, name, phone, email, standard_pizzas=None, custom_pizzas=None, side_dishes=None) -> None:
    Order.no_of_orders += 1
    self.__order_num = Order.no_of_orders
    self.__name = name
    self.__phone = phone
    self.__email = email
    self.__standard_pizzas = standard_pizzas if standard_pizzas is not None else []
    self.__custom_pizzas = custom_pizzas if custom_pizzas is not None else []
    self.__side_dishes = side_dishes if side_dishes is not None else []

  def __str__(self) -> str:
    output = f"Order Number: {self.__order_num}\nCustomer Name: {self.__name}\nCustomer Phone: {self.__phone}\nCustomer Email: {self.__email}\n"
    if self.__standard_pizzas:
      output += "\nList of Pizza Ordered:\n"
      for standard_pizza in self.__standard_pizzas:
        output += standard_pizza + "\n"
    if self.__custom_pizzas:
      output += "\nList of Custom Pizza Ordered:\n"
      for custom_pizza in self.__custom_pizzas:
        output += custom_pizza + "\n"
    if self.__side_dishes:
      output += "List of Side Dishes Ordered:\n"
      for side_dish in self.__side_dishes:
        output += side_dish + "\n"
    return output
from pizza_menu_item import PizzaMenuItem
from custom_pizza_item import CustomPizzaItem
from side_dish import SideDish

class Order:
  no_of_orders = 0

  def __init__(self, name, phone, email, standard_pizzas=None, custom_pizzas=None, side_dishes=None, processed=False) -> None:
    Order.no_of_orders += 1
    self.__order_num = Order.no_of_orders
    self.__name = name
    self.__phone = phone
    self.__email = email
    self.__standard_pizzas = standard_pizzas if standard_pizzas is not None else []
    self.__custom_pizzas = custom_pizzas if custom_pizzas is not None else []
    self.__side_dishes = side_dishes if side_dishes is not None else []
    self.__processed = processed
    self.__price = self.calculate_price()

  @property
  def order_num(self) -> int:
    return self.__order_num

  @property
  def name(self) -> str:
    return self.__name

  @property
  def phone(self) -> str:
    return self.__phone

  @property
  def email(self) -> str:
    return self.__email

  @property
  def standard_pizzas(self) -> list[PizzaMenuItem]:
    return self.__standard_pizzas

  @property
  def custom_pizzas(self) -> list[CustomPizzaItem]:
    return self.__custom_pizzas

  @property
  def side_dishes(self) -> list[SideDish]:
    return self.__side_dishes

  @property
  def processed(self) -> bool:
    return self.__processed

  @processed.setter
  def processed(self, processed: bool) -> None:
    self.__processed = processed

  def kitchen_slip(self) -> str:
    output = f"Order Number: {self.__order_num}\n"
    sections = []
    if self.__standard_pizzas:
        standard_pizzas_str = "List of Pizza to Prepare:"
        for pizza in self.__standard_pizzas:
          recipe_str = " ".join(f"{ingredient}({quantity})" for ingredient, quantity in pizza.recipe.ingredients.items())
          standard_pizzas_str += f"\n{pizza.name} {pizza.size}\nIngredients in Recipe: {recipe_str}"
        sections.append(standard_pizzas_str)
    if self.__custom_pizzas:
        custom_pizzas_str = "List of Custom Pizza to Prepare:"
        for pizza in self.__custom_pizzas:
            toppings_str = " ".join(f"{ingredient}({quantity})" for ingredient, quantity in pizza.ingredients.items())
            custom_pizzas_str += f"\n{pizza.size} {pizza.crust} {pizza.sauce}\nToppings: {toppings_str}"
        sections.append(custom_pizzas_str.strip())
    if self.__side_dishes:
        side_dishes_str = "List of Side Dishes to Prepare:"
        side_dishes_str += "\n" + " | ".join(f"{dish.name}" for dish in self.__side_dishes)
        sections.append(side_dishes_str)
    output += "\n" + "\n\n".join(sections)
    return output

  def calculate_price(self) -> float:
    price = 0
    for standard_pizza in self.__standard_pizzas:
      price += standard_pizza.price
    for custom_pizza in self.__custom_pizzas:
      price += custom_pizza.price
    for side_dish in self.__side_dishes:
      price += side_dish.price
    return round(price, 2)

  def receipt(self) -> str:
    output = f"Order Number: {self.__order_num}\nCustomer Name: {self.__name}\nCustomer Phone: {self.__phone}\nCustomer Email: {self.__email}\n"
    sections = []
    if self.__standard_pizzas:
      standard_pizzas_str = "\nList of Pizza Ordered:"
      standard_pizzas_str += "\n" + "\n".join(f"{pizza.name} {pizza.size} | ${pizza.price}" for pizza in self.__standard_pizzas)
      sections.append(standard_pizzas_str)
    if self.__custom_pizzas:
      custom_pizzas_str = "\nList of Custom Pizza Ordered:"
      for pizza in self.__custom_pizzas:
        toppings_str = " ".join(f"{ingredient}({quantity})" for ingredient, quantity in pizza.ingredients.items())
        custom_pizzas_str += f"\n{pizza.size} {pizza.crust} {pizza.sauce}\n{toppings_str}\nTotal for this pizza: ${pizza.price}"
      sections.append(custom_pizzas_str)
    if self.__side_dishes:
      side_dishes_str = "\nList of Side Dishes Ordered:"
      side_dishes_str += "\n" + "\n".join(f"{dish.name} | ${dish.price}" for dish in self.__side_dishes)
      sections.append(side_dishes_str)
    output += "\n".join(sections)
    output += f"\n\nTotal Price: ${self.__price}"
    return output

  def __str__(self) -> str:
    output = f"Order Number: {self.__order_num}\nCustomer Name: {self.__name}\nCustomer Phone: {self.__phone}\nCustomer Email: {self.__email}"
    sections = []
    if self.__standard_pizzas:
      standard_pizzas_str = "List of Pizza Ordered:"
      standard_pizzas_str += "\n" + "\n\n".join(pizza.__str__() for pizza in self.__standard_pizzas)
      sections.append(standard_pizzas_str)
    if self.__custom_pizzas:
      custom_pizzas_str = "List of Custom Pizza Ordered:"
      custom_pizzas_str += "\n" + "\n\n".join(pizza.__str__() for pizza in self.__custom_pizzas)
      sections.append(custom_pizzas_str)
    if self.__side_dishes:
      side_dishes_str = "List of Side Dishes Ordered:"
      side_dishes_str += "\n" + "\n\n".join(side.__str__() for side in self.__side_dishes)
      sections.append(side_dishes_str)
    output += "\n\n" + "\n\n".join(sections)
    return output.strip()
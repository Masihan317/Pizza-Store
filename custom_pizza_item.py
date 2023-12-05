from enum import Enum

class CustomPizzaSize(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

class CustomPizzaCrust(Enum):
  ORIGINAL = 1
  THIN = 2
  GLUTEN_FREE = 3

class CustomPizzaSauce(Enum):
  MARINARA = 1
  BBQ_SAUCE = 2
  ALFREDO_SAUCE = 3

class CustomPizzaItem:
  def __init__(self, size: CustomPizzaSize, crust: CustomPizzaCrust, sauce: CustomPizzaSauce, ingredients: dict[str, int]) -> None:
    self.__size = size
    self.__crust = crust
    self.__sauce = sauce
    self.__ingredients = ingredients
    self.__price = self.calculate_price()

  @property
  def size(self) -> CustomPizzaSize:
    return self.__size

  @property
  def crust(self) -> CustomPizzaCrust:
    return self.__crust

  @property
  def sauce(self) -> CustomPizzaSauce:
    return self.__sauce

  @property
  def ingredients(self) -> dict[str, int]:
    return self.__ingredients

  @property
  def price(self) -> float:
    return self.__price

  def __str__(self) -> str:
    output = f"Custom Pizza Information:\nSize: {self.__size}\nCrust: {self.__crust}\nSauce: {self.__sauce}\nList of Ingredients:\n"
    for ingredient, quantity in self.__ingredients.items():
      output += f"Ingredient Name: {ingredient} | Quantity Needed: {quantity}\n"
    return output.strip()

  def calculate_price(self) -> float:
    ingredient_num = 0
    for _, quantity in self.__ingredients.items():
      ingredient_num += quantity
    ingredients_price = 1.75 * ingredient_num
    if self.__size == "SMALL":
      return 10.00 + ingredients_price
    elif self.__size == "MEDIUM":
      return 12.00 + ingredients_price
    elif self.__size == "LARGE":
      return 14.00 + ingredients_price
from enum import Enum
from pizza_recipe import PizzaRecipe

class PizzaSize(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

class PizzaCategory(Enum):
  VEGETARIAN = 1
  MEATLOVERS = 2
  SPECIALTY = 3

class PizzaMenuItem:
  def __init__(self, name: str, description: str, price: float, size: PizzaSize, recipe: PizzaRecipe, category: PizzaCategory) -> None:
    self.__name = name
    self.__description = description
    self.__price = price
    self.__size = size
    self.__recipe = recipe
    self.__category = category

  @property
  def name(self) -> str:
    return self.__name

  @property
  def description(self) -> str:
    return self.__description

  @property
  def price(self) -> float:
    return self.__price

  @property
  def size(self) -> PizzaSize:
    return self.__size

  @property
  def recipe(self) -> PizzaRecipe:
    return self.__recipe

  @property
  def category(self) -> PizzaCategory:
    return self.__category

  @name.setter
  def name(self, name: str) -> None:
    self.__name = name

  @description.setter
  def description(self, description: str) -> None:
    self.__description = description

  @price.setter
  def price(self, price: float) -> None:
    self.__price = price

  @size.setter
  def size(self, size: PizzaSize) -> None:
    self.__size = size

  @recipe.setter
  def recipe(self, recipe: PizzaRecipe) -> None:
    self.__recipe = recipe

  @category.setter
  def category(self, category: PizzaCategory) -> None:
    self.__category = category

  def __str__(self) -> str:
    return f"Pizza Name: {self.__name}\nDescription: {self.__description}\nPrice: {self.__price}\nSize: {self.__size}\nCategory: {self.__category}\n{self.__recipe}"

  def to_list(self) -> list[str]:
    lst: list[str] = []
    lst.append(self.__name)
    lst.append(self.__description)
    lst.append(self.__price)
    lst.append(self.__size)
    lst.append(self.__recipe.name)
    lst.append(self.__category)
    return lst

  def __eq__(self, __value: object) -> bool:
    if isinstance(__value, PizzaMenuItem):
      return self.__name == __value.__name
    return False
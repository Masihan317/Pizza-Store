from enum import Enum

class SideDishType(Enum):
  APPETIZER = 1
  DESSERT = 2
  BEVERAGE = 3

class SideDish:
  def __init__(self, name: str, description: str, price: float, type: SideDishType) -> None:
    self.__name = name
    self.__description = description
    self.__price = price
    self.__type = type

  def __str__(self) -> str:
    return f"Side Name: {self.__name}\nDescription: {self.__description}\nPrice: {self.__price}\nType: {self.__type}"

  @property
  def name(self) -> str:
    return self.__name

  @property
  def type(self) -> SideDishType:
    return self.__type

  def to_list(self):
    lst: list[str] = []
    lst.append(self.__name)
    lst.append(self.__description)
    lst.append(self.__price)
    lst.append(self.__type)
    return lst

  def __eq__(self, __value: object) -> bool:
    if isinstance(__value, SideDish):
      return self.__name == __value.__name
    return False
class Ingredient:
  def __init__(self, name: str, quantity: int, reorder_level: int) -> None:
    self.__name = name
    self.__quantity = quantity
    self.__reorder_level = reorder_level

  def __str__(self) -> str:
    return f"Ingredient Name: {self.__name}\nQuantity: {self.__quantity}\nReorder Level: {self.__reorder_level}"

  @property
  def name(self) -> str:
    return self.__name

  @property
  def quantity(self) -> int:
    return self.__quantity

  @property
  def reorder_level(self) -> int:
    return self.__reorder_level

  @quantity.setter
  def quantity(self, quantity: int) -> None:
    self.__quantity = quantity

  def to_list(self):
    lst: list[str] = []
    lst.append(self.__name)
    lst.append(self.__quantity)
    lst.append(self.__reorder_level)
    return lst

  def __eq__(self, __value: object) -> bool:
    if isinstance(__value, Ingredient):
      return self.__name == __value.__name
    return False
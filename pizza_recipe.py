class PizzaRecipe:
  def __init__(self, name: str, ingredients: dict[str, int]) -> None:
    self.__name = name
    self.__ingredients = ingredients

  def __str__(self) -> str:
    output = f"Recipe Name: {self.__name}\nList of Ingredients:\n"
    for ingredient, quantity in self.__ingredients.items():
      output += f"Ingredient Name: {ingredient} | Quantity Needed: {quantity}\n"
    return output.strip()

  @property
  def name(self) -> str:
    return self.__name

  @property
  def ingredients(self) -> dict[str, int]:
    return self.__ingredients

  @ingredients.setter
  def ingredients(self, ingredients) -> None:
    self.__ingredients = ingredients

  def to_list(self) -> list[str]:
    lst: list[str] = []
    lst.append(self.__name)
    for ingredient, quantity in self.__ingredients.items():
      lst.append(ingredient)
      lst.append(quantity)
    return lst

  def __eq__(self, __value: object) -> bool:
    if isinstance(__value, PizzaRecipe):
      return self.__name == __value.__name
    return False
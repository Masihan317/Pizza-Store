from pizza_menu_item import *
from pizza_menu_repository import PizzaMenuRepository

class PizzaMenuManager:
  def __init__(self) -> None:
    self.__menu_items: list[PizzaMenuItem] = []

  def add_menu_item(self, menu_item: PizzaMenuItem):
    self.__menu_items.append(menu_item)

  def remove_menu_item(self, name: str):
    for menu_item in self.__menu_items:
      if menu_item.name == name:
        self.__menu_items.remove(menu_item)

  def update_menu_item(self, name: str, new_menu_item: PizzaMenuItem):
    for menu_item in self.__menu_items:
      if menu_item.name == name:
        menu_item.description = new_menu_item.description
        menu_item.price = new_menu_item.price
        menu_item.size = new_menu_item.size
        menu_item.recipe = new_menu_item.recipe
        menu_item.category = new_menu_item.category

  def get_menu_items_by_name(self, name: str, size: PizzaSize) -> PizzaMenuItem:
    for menu_item in self.__menu_items:
      if menu_item.name == name and menu_item.size == size:
        return menu_item

  def get_menu_items_by_category(self, category: PizzaCategory) -> list[PizzaMenuItem]:
    menu_items = []
    for menu_item in self.__menu_items:
      if menu_item.category == category:
        menu_items.append(menu_item)
    return menu_items

  def list_menu_items(self):
    for menu_item in self.__menu_items:
      print(menu_item)

  def save_to_file(self) -> None:
    repository = PizzaMenuRepository("pizza_menu.csv")
    repository.save_pizza_menu(self.__menu_items)

  def read_from_file(self) -> None:
    repository = PizzaMenuRepository("pizza_menu.csv")
    self.__menu_items = repository.load_pizza_menu()
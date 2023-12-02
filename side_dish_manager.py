from side_dish import *
from side_dish_repository import SideDishRepository

class SideDishManager:
  def __init__(self) -> None:
    self.__side_dishes: list[SideDish] = []

  def add_side_dishes(self, side_dishes: SideDish):
    self.__side_dishes.append(side_dishes)

  def remove_side_dishes(self, side_dish_name: str):
    for side_dish in self.__side_dishes:
      if side_dish.name == side_dish_name:
        self.__side_dishes.remove(side_dish)

  def get_side_dishes_by_name(self, side_dish_name: str) -> SideDish:
    for side_dish in self.__side_dishes:
      if side_dish.name == side_dish_name:
        return side_dish

  def get_side_dishes_by_type(self, side_dish_type: SideDishType) -> list[SideDish]:
    dishes = []
    for side_dish in self.__side_dishes:
      if side_dish.type == side_dish_type:
        dishes.append(side_dish)
    return dishes

  def list_side_dishes(self):
    for side_dish in self.__side_dishes:
      print(side_dish)

  def save_to_file(self) -> None:
    repository = SideDishRepository("side_dishes.csv")
    repository.save_side_dishes(self.__side_dishes)

  def read_from_file(self) -> None:
    repository = SideDishRepository("side_dishes.csv")
    self.__side_dishes = repository.load_side_dishes()
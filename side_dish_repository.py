from side_dish import SideDish
import csv

class SideDishRepository:
  def __init__(self, filename: str) -> None:
    self.__filename = filename

  def save_side_dishes(self, side_dishes: list[SideDish]) -> None:
    with open(self.__filename, "w", newline="") as file:
      writer = csv.writer(file)
      for side_dish in side_dishes:
        writer.writerow(side_dish.to_list())

  def load_side_dishes(self) -> list[SideDish]:
    with open(self.__filename, newline="") as file:
      reader = csv.reader(file)
      side_dishes = []
      for row in reader:
        side_dish = SideDish(row[0], row[1], float(row[2]), row[3])
        side_dishes.append(side_dish)
    return side_dishes
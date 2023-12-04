from custom_pizza_item import *      

custom_pizza_info = "There's an option to create your own pizza.\n"
custom_pizza_info += "Please pick a size:\n"
custom_pizza_info +=" | ".join([size.name for size in CustomPizzaSize])
custom_pizza_info += "\nPlease pick a crust:\n"
custom_pizza_info +=" | ".join([crust.name for crust in CustomPizzaCrust])
custom_pizza_info += "\nPlease pick a sauce:\n"
custom_pizza_info +=" | ".join([sauce.name for sauce in CustomPizzaSauce])
print(custom_pizza_info)
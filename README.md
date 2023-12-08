# Pizza-Store

### Introduction
Object-Oriented approach to develop a comprehensive pizza store application that streamlines recipe management, inventory control, menu customization, order processing, empowering the store owner to manage their business effectively.

### Installation
Clone the repository or download directly.
```
git clone https://github.com/Masihan317/Pizza-Store.git
cd Pizza-Store
```

### Usage
Run the following command to start the application.
```
python3 pizza_store.py
```
Or you could also just click the Run button on VSCode :D
Do whatever floats your boat!

### Application Manual
The main menu looks something like this:
```
Pizza Store Menu (Please enter a number from 1 to 6.)
1. Recipe Manager System
2. Ingredient Inventory System
3. Pizza Menu Manager System
4. Side Dish Menu Manager System
5. Order Manager System
6. Quit
```

You can enter a number to go into a sub-menu/system.
1. Recipe Manager System
```
Welcome to the Recipe Manager System!
Recipe Manager Menu (Please enter a number from 1 to 6.)
1. Add Recipe
2. Remove Recipe
3. Update Recipe
4. Search Recipe
5. List Recipes
6. Return to Pizza Store Application
```

- The user can add, remove, update, search, and list the recipes available.
- When adding a new recipe, the user will be asked to enter the name of the recipe. The user will then need to input the name and quantity of each ingredient. (Note that the ingredient being used in the recipe must be available in the inventory.)

2. Ingredient Inventory System
```
Welcome to the Ingredient Inventory System!
Ingredient Inventory Menu (Please enter a number from 1 to 5.)
1. Add Ingredient
2. Remove Ingredient
3. Check Ingredient Supply
4. List Ingredients
5. Return to Pizza Store Application
```

- When prompted to add the ingredients, the users will be asked the name, quantity, reorder level, and unit (1/2 cup, slice, 1/4 cup etc.) which represents what the unit of the quantity is. After the user types this information it will be recorded and saved to the file when the user returns to the pizza store application.
- If the user wants to remove some ingredients it's also possible. The user will be ask what ingredient and how much to remove. (If the number reaches 0 the ingredient will be removed from the list.)
- The check supply option will print a message if the quantity is lower than the reorder level.

3. Pizza Menu Manager System
```
Welcome to the Pizza Menu Manager System! (Please enter a number from 1 to 8.)
1. Add Pizza Menu Item
2. Remove Pizza Menu Item
3. Update Pizza Menu Item
4. Search Pizza Menu Item by Name
5. Get Pizza Menu Item by Category
6. List All Pizza Menu Item
7. List Custom Pizza Item Options
8. Return to Pizza Store Application
```

- The user can add, remove, update, search (by name and size or by category), and list all of the pizza menu items.
- The user will be asked to enter the name, description, size, price, size, recipe name, and category of the pizza.
- When searching pizza recipes by name, the user will need to enter both the name and the size because the same pizza of different sizes are considered different menu items for price calculation purposes.
- The recipe name entered must be a recipe that exists in the Recipe Manager.
- There's also an option to list the custom pizza item options, which shows the size, crust, sauce, and available toppings. (This is a menu that the store owner can show to the customers directly. Note each topping selected is $1.75 but this price can be easily changed.)

Here's what an example looks like (As ingredients are added and removed the list of available ingredients might change.):
```
There's an option to create your own pizza.
Please pick a size:
SMALL | MEDIUM | LARGE
Please pick a crust:
ORIGINAL | THIN | GLUTEN_FREE
Please pick a sauce:
MARINARA | BBQ_SAUCE | ALFREDO_SAUCE
Please pick your toppings:
Pepperoni | Ham | Bacon | Mushroom | Onion | Olive | Tomato | Cheddar | Pineapple | Pepper | Chicken
```

4. Side Dish Menu Manager System
```
Welcome to the Side Dish Manager System!
Side Dish Manager Menu (Please enter a number from 1 to 6.)
1. Add Side Dish
2. Remove Side Dish
3. Search Side Dish by Name
4. Get Side Dishes by Type
5. List All Side Dishes
6. Return to Pizza Store Application
```

- The user can add, remove, search (by name or by type), and list all of the side dish items.
- When adding a new side dish, the user needs to enter the name, description, price, and type.
- There are currently 3 types of side dishes (DESSERT, APPETIZER, BEVERAGE) but more types can be added.

5. Order Manager System
```
Welcome to the Order Manager System! (Please enter a number from 1 to 11.)
1. Add Order
2. Remove Order
3. Process Order
4. Process All Orders
5. Display Order Detail
6. Display Order Details for All Orders
7. Generate Order Slips for Kitchen
8. Generate All Order Slips for Kitchen
9. Print Customer Receipt
10. Print All Receipts
11. Return to Pizza Store Application
```

- The user can add, remove, process orders (one order or all orders), display order details (one or all), print receipts (one or all orders), and generate kitchen slips for staff (one or all).
- An order contains customer name, phone, email, list of standard/customized pizzas, side dishes and a process status. When the user wants to add an order they will be prompted to enter those data.
- When an order gets processed, the corresponding ingredients will be deducted from the inventory according to the recipes. The order will then be marked processed. A processed order will not be processed again.
- The order objects are stored in a custom json format.
- More examples of what an order object looks like is shown in the example test cases section.

The menu itself is quite self-explanatory with existing data in csv or json files. The user can enter numbers to navigate back and forth between the application and the sub-systems.

### Example Test Cases
Since the main purpose of this application is for the store owner to efficiently process customer orders, I am going to focus on showing what orders look like in the system. (Adding ingredients, recipes, pizza menu items, and side dishes are very self-explanatory with the prompts in the program so I am going to skip over those.)

There are 3 orders already in the orders.json file. I am going to showcase order no.1 because it is the one with all 3 types of order items (standard pizza orders, custom pizza orders, and side dish orders). The standard pizza, custom pizza, and side dish orders are all lists that stores json objects where each object corresponds to an order item. You can print order 2 and 3 as well but since it will get the md file too long, I'll skip here. (You can do so by printing one order by giving the order number or every order in the system.)

```
{
      "name": "Jamie",
      "phone": "4358738273",
      "email": "jding@gmail.com",
      "standard_pizza": [
        {
          "name": "Pepperoni Pizza",
          "size": "SMALL"
        },
        {
          "name": "Deluxe Pizza",
          "size": "MEDIUM"
        }
      ],
      "custom_pizza": [
        {
          "size": "MEDIUM",
          "crust": "ORIGINAL",
          "sauce": "MARINARA",
          "ingredients": {
            "Mushroom": 2,
            "Bacon": 2,
            "Ham": 3
          }
        }
      ],
      "side_dish": [
        "Chocolate Donut Bites"
      ],
      "processed": false
    }
```

This json object corresponds to a customer named Jamie with phone number 4358738273 and email address jding@gmail.com. She also ordered 2 standard pizzas, one small pepperoni pizza and one medium deluxe pizza. She ordered one custom MEDIUM sized pizza with ORIGINAL crust and MARINARA sauce. The toppings on that custom pizza is 2 servings of mushrooms, 2 servings of bacon, and 3 servings of ham. She also ordered a side of chocolate donut bites. Since it's just a test object it's not processed. After I process the order the processed attribute will show true. Processing the order will also use the corresponding ingredients in the inventory.

List of ingredient used:
Small pepperoni pizza used 5 servings of pepperoni.
Medium deluxe pizza used 4 servings of pepperoni, 5 servings of bacon, 3 servings of mushroom, 2 servings of olive, 4 servings of pepper, and 5 servings of onion.
The custom medium original marinara pizza had 3 servings of mushroom, 2 servings of bacon, and 3 servings of ham.
A total of 9 servings of pepperoni, 7 servings of bacon, 5 servings of mushroom, 2 servings of olive, 4 servings of pepper, 5 servings of onion, and 3 servings of ham are used.

Sample inventory file (ingredients.csv) before processing order 1:
```
Pepperoni,100,10,1/2 cup
Ham,100,10,slice
Bacon,100,10,slice
Mushroom,100,10,1/2 cup
Onion,100,10,1/4 cup
Olive,100,10,1/4 cup
Tomato,100,10,1/2 cup
Cheddar,100,10,1/4 cup
Pineapple,100,10,1/4 cup
Pepper,100,10,1/4 cup
Chicken,100,10,1/2 cup
```

Sample inventory file (ingredients.csv) after processing order 1:
```
Pepperoni,91,10,1/2 cup
Ham,97,10,slice
Bacon,93,10,slice
Mushroom,95,10,1/2 cup
Onion,95,10,1/4 cup
Olive,98,10,1/4 cup
Tomato,100,10,1/2 cup
Cheddar,100,10,1/4 cup
Pineapple,100,10,1/4 cup
Pepper,96,10,1/4 cup
Chicken,100,10,1/2 cup
```

Sample Order Details for Order 1
```
Order Number: 1
Customer Name: Jamie
Customer Phone: 4358738273
Customer Email: jding@gmail.com
Order Processed?: False

List of Pizza Ordered:
Pizza Name: Pepperoni Pizza
Description: Indulge in our Pepperoni Bliss: a crispy crust layered with rich tomato sauce, melted mozzarella, and spicy, savory pepperoni slices for a classic taste adventure.
Price: 11.5
Size: SMALL
Category: MEATLOVERS
Recipe Name: Pepperoni
List of Ingredients:
Ingredient Name: Pepperoni | Quantity Needed: 5

Pizza Name: Deluxe Pizza
Description: Feast on our Deluxe Pizza, a gourmet medley of fresh bell peppers, savory onions, succulent mushrooms, pepperoni, and Italian sausage, all atop a golden, cheesy crust.
Price: 17.5
Size: MEDIUM
Category: SPECIALTY
Recipe Name: Deluxe
List of Ingredients:
Ingredient Name: Pepperoni | Quantity Needed: 4
Ingredient Name: Bacon | Quantity Needed: 5
Ingredient Name: Mushroom | Quantity Needed: 3
Ingredient Name: Olive | Quantity Needed: 2
Ingredient Name: Pepper | Quantity Needed: 4
Ingredient Name: Onion | Quantity Needed: 5

List of Custom Pizza Ordered:
Custom Pizza Information:
Size: MEDIUM
Crust: ORIGINAL
Sauce: MARINARA
List of Ingredients:
Ingredient Name: Mushroom | Quantity Needed: 2
Ingredient Name: Bacon | Quantity Needed: 2
Ingredient Name: Ham | Quantity Needed: 3

List of Side Dishes Ordered:
Side Name: Chocolate Donut Bites
Description: Warm, chocolatey cake-donut bites stuffed with a decadent chocolate filling & tossed in sugar.
Price: 9.49
Type: DESSERT
```

Sample Kitchen Slip (for staff to prepare order) for Order 1
```
Order Number: 1

List of Pizza to Prepare:
Pepperoni Pizza SMALL
Ingredients in Recipe: Pepperoni(5)
Deluxe Pizza MEDIUM
Ingredients in Recipe: Pepperoni(4) Bacon(5) Mushroom(3) Olive(2) Pepper(4) Onion(5)

List of Custom Pizza to Prepare:
MEDIUM ORIGINAL MARINARA
Toppings: Mushroom(2) Bacon(2) Ham(3)

List of Side Dishes to Prepare:
Chocolate Donut Bites
```

Sample Receipt for Order 1
```
Order Number: 1
Customer Name: Jamie
Customer Phone: 4358738273
Customer Email: jding@gmail.com

List of Pizza Ordered:
Pepperoni Pizza SMALL | $11.5
Deluxe Pizza MEDIUM | $17.5

List of Custom Pizza Ordered:
MEDIUM ORIGINAL MARINARA
Mushroom(2) Bacon(2) Ham(3)
Total for this pizza: $24.25

List of Side Dishes Ordered:
Chocolate Donut Bites | $9.49

Total Price: $62.74
```

Thank you! I hope you enjoyed reading this manual! :D
const COOKING_RECIPES_DATA = [
  {
    "name": "Mayonnaise (S)",
    "iconKey": "Mayonnaise S",
    "req_ingredients": "Regular Quality Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (M)",
    "iconKey": "Mayonnaise M",
    "req_ingredients": "Good Quality Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (L)",
    "iconKey": "Mayonnaise L",
    "req_ingredients": "High Quality Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (G)",
    "iconKey": "Mayonnaise G",
    "req_ingredients": "Golden Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (P)",
    "iconKey": "Mayonnaise P",
    "req_ingredients": "P Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (X)",
    "iconKey": "Mayonnaise X",
    "req_ingredients": "X Egg, Oil",
    "req_utensils": "Whisk",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Mayonnaise (X)",
    "iconKey": "Mayonnaise X",
    "req_ingredients": "Mayonnaise (S), Mayonnaise (M), Mayonnaise (L), Mayonnaise (G), Mayonnaise (P)",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "X Egg",
    "iconKey": "X Egg",
    "req_ingredients": "Regular Quality Egg, Good Quality Egg, High Quality Egg, Golden Egg, P Egg",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Milk (X)",
    "iconKey": "Milk X",
    "req_ingredients": "Milk (S), Milk (M), Milk (L), Milk (G), Milk (P)",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Cheese (X)",
    "iconKey": "Cheese X",
    "req_ingredients": "Cheese (S), Cheese (M), Cheese (L), Cheese (G), Cheese (P)",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Wild Grape Juice",
    "iconKey": "Grape Juice",
    "req_ingredients": "Wild Grape, Wine, Purple Grass",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Pickles",
    "iconKey": "Pickles",
    "req_ingredients": "Cucumber",
    "req_utensils": "-",
    "req_seasoning": "Salt"
  },
  {
    "name": "Salad",
    "iconKey": "Salad",
    "req_ingredients": "One or more of: Cucumber Cabbage Tomato Carrot",
    "req_utensils": "Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Curry Rice",
    "iconKey": "Curry Rice",
    "req_ingredients": "Rice Balls, Curry Powder",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Stew",
    "iconKey": "Stew",
    "req_ingredients": "Flour, any Milk",
    "req_utensils": "Pot",
    "req_seasoning": "Salt"
  },
  {
    "name": "Miso Soup",
    "iconKey": "Miso Soup",
    "req_ingredients": "One or more of: Bamboo Shoot Mushroom Truffle Turnip Corn Carrot Eggplant Onion Tomato",
    "req_utensils": "Pot",
    "req_seasoning": "Miso, Salt"
  },
  {
    "name": "Stir Fry",
    "iconKey": "Stir-Fried Vegetables",
    "req_ingredients": "Oil, Cabbage",
    "req_utensils": "Knife, Frying Pan",
    "req_seasoning": "Soy Sauce"
  },
  {
    "name": "Fried Rice",
    "iconKey": "Fried Rice",
    "req_ingredients": "Rice Balls, any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Savory Pancake",
    "iconKey": "Okonomiyaki",
    "req_ingredients": "Cabbage, Oil, Flour, Egg",
    "req_utensils": "Frying Pan, Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Sandwich",
    "iconKey": "Sandwich",
    "req_ingredients": "Bread, one or more of: Boiled Egg Cucumber Tomato",
    "req_utensils": "Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Fruit Juice",
    "iconKey": "Fruit Juice",
    "req_ingredients": "One or more of: Any Apple Strawberry Pineapple Wild Grapes",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Fruit Latte",
    "iconKey": "Fruit Latte",
    "req_ingredients": "Any Milk, one or more of: Any Apple Strawberry Pineapple Wild Grapes",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Vegetable Juice",
    "iconKey": "Vegetable Juice",
    "req_ingredients": "One or more of: Cucumber Cabbage Carrot Onion Spinach",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Vegetable Latte",
    "iconKey": "Vegetable Latte",
    "req_ingredients": "Any Milk, one or more of: Cucumber Cabbage Carrot Turnip Onion Green Pepper Spinach Tomato",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Mixed Juice",
    "iconKey": "Mixed Juice",
    "req_ingredients": "Vegetable Juice, Fruit Juice",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Mixed Latte",
    "iconKey": "Mixed Latte",
    "req_ingredients": "Mixed Juice, any Milk",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Pickled Turnip",
    "iconKey": "Pickled Turnip",
    "req_ingredients": "Turnips",
    "req_utensils": "Knife",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "French Fries",
    "iconKey": "French Fries",
    "req_ingredients": "Potato, Oil",
    "req_utensils": "Frying Pan, Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Strawberry Jam",
    "iconKey": "Strawberry Jam",
    "req_ingredients": "Strawberry",
    "req_utensils": "Pot",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Strawberry Milk",
    "iconKey": "Strawberry Smoothie",
    "req_ingredients": "Strawberry, any Milk",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Tomato Juice",
    "iconKey": "Tomato Juice",
    "req_ingredients": "Tomato",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Popcorn",
    "iconKey": "Popcorn",
    "req_ingredients": "Corn, Butter",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Corn Flakes",
    "iconKey": "Corn Flakes",
    "req_ingredients": "Corn",
    "req_utensils": "Oven,&#160; Rolling Pin",
    "req_seasoning": "-"
  },
  {
    "name": "Baked Corn",
    "iconKey": "Roasted Corn",
    "req_ingredients": "Corn",
    "req_utensils": "Oven",
    "req_seasoning": "-"
  },
  {
    "name": "Pineapple Juice",
    "iconKey": "Pineapple Juice",
    "req_ingredients": "Pineapple",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Pumpkin Pudding",
    "iconKey": "Pumpkin Pudding",
    "req_ingredients": "Any Egg, any Milk, Pumpkin",
    "req_utensils": "Pot, Oven",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Pumpkin Stew",
    "iconKey": "Pumpkin Stew",
    "req_ingredients": "Pumpkin",
    "req_utensils": "Pot",
    "req_seasoning": "Sugar, Soy Sauce"
  },
  {
    "name": "Happy Eggplant",
    "iconKey": "Happy Eggplant",
    "req_ingredients": "Eggplant",
    "req_utensils": "Frying Pan",
    "req_seasoning": "Sugar, Soy Sauce, Miso"
  },
  {
    "name": "Sweet Potatoes",
    "iconKey": "Sweet Potato",
    "req_ingredients": "Butter, any Egg, Sweet Potato",
    "req_utensils": "Pot, Oven",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Baked Sweet Potato",
    "iconKey": "Roasted Sweet Potato",
    "req_ingredients": "Sweet Potato",
    "req_utensils": "Oven",
    "req_seasoning": "-"
  },
  {
    "name": "Greens",
    "iconKey": "Green Vegetables",
    "req_ingredients": "Spinach",
    "req_utensils": "Pot",
    "req_seasoning": "Soy Sauce"
  },
  {
    "name": "Scrambled Eggs",
    "iconKey": "Scrambled Eggs",
    "req_ingredients": "Any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Omelet",
    "iconKey": "Omelet",
    "req_ingredients": "Any Egg, any Milk, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Omelet Rice",
    "iconKey": "Omelet Rice",
    "req_ingredients": "Any Egg, any Milk, Oil, Rice Ball",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Boiled Egg",
    "iconKey": "Boiled Egg",
    "req_ingredients": "Egg",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Pudding",
    "iconKey": "Pudding",
    "req_ingredients": "Any Egg, any Milk",
    "req_utensils": "Pot, Oven",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Hot Milk",
    "iconKey": "Hot Milk",
    "req_ingredients": "Any Milk",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Butter",
    "iconKey": "Butter",
    "req_ingredients": "Any Milk",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Cheese Cake",
    "iconKey": "Cheesecake",
    "req_ingredients": "Any Cheese, any Egg, any Milk",
    "req_utensils": "Pot, Oven, Whisk",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Cheese Fondue",
    "iconKey": "Cheese Fondue",
    "req_ingredients": "Cheese, Bread",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Apple Pie",
    "iconKey": "Apple Pie",
    "req_ingredients": "Any Apple, any Egg, Butter, Flour",
    "req_utensils": "Pot, Oven, Knife, Rolling Pin",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Apple Jam",
    "iconKey": "Apple Jam",
    "req_ingredients": "Any Apple",
    "req_utensils": "Pot",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Apple Souffle",
    "iconKey": "Apple Souffle",
    "req_ingredients": "Any Apple",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Bamboo Rice",
    "iconKey": "Bamboo Rice",
    "req_ingredients": "Bamboo Shoot, Rice Ball",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Grape Jam",
    "iconKey": "Grape Jam",
    "req_ingredients": "Wild Grape",
    "req_utensils": "Pot",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Grape Juice",
    "iconKey": "Grape Juice",
    "req_ingredients": "Wild Grape",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Mushroom Rice",
    "iconKey": "Mushroom Rice",
    "req_ingredients": "Mushroom, Rice Ball",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Truffle Rice",
    "iconKey": "Truffle Rice",
    "req_ingredients": "Truffle, Rice Ball",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Sushi",
    "iconKey": "Sushi",
    "req_ingredients": "Sashimi, Rice Ball",
    "req_utensils": "-",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Jam Bun",
    "iconKey": "Jam Bun",
    "req_ingredients": "Bread, any Jam",
    "req_utensils": "-",
    "req_seasoning": "Sugar, Salt"
  },
  {
    "name": "Dinner Roll",
    "iconKey": "Dinner Roll",
    "req_ingredients": "Bread, Butter",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Raisin Bread",
    "iconKey": "Raisin Bread",
    "req_ingredients": "Bread, Wild Grapes",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Curry Bread",
    "iconKey": "Curry Bread",
    "req_ingredients": "Bread, Curry Powder, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Toast",
    "iconKey": "Toast",
    "req_ingredients": "Bread",
    "req_utensils": "Oven",
    "req_seasoning": "-"
  },
  {
    "name": "French Toast",
    "iconKey": "French Toast",
    "req_ingredients": "Bread, any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Sashimi",
    "iconKey": "Sashimi",
    "req_ingredients": "Medium Fish or Large Fish",
    "req_utensils": "Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Grilled Fish",
    "iconKey": "Grilled Fish",
    "req_ingredients": "Medium Fish, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Chirashi Sushi",
    "iconKey": "Mixed Sashimi",
    "req_ingredients": "Scrambled Eggs, Sashimi, Rice Ball",
    "req_utensils": "Knife",
    "req_seasoning": "Vinegar"
  },
  {
    "name": "Pizza",
    "iconKey": "Pizza",
    "req_ingredients": "Cheese, Flour, Ketchup, Mushroom, Onion, Tomato",
    "req_utensils": "Oven, Rolling Pin",
    "req_seasoning": "Salt"
  },
  {
    "name": "Noodles",
    "iconKey": "Noodles",
    "req_ingredients": "Flour",
    "req_utensils": "Pot, Rolling Pin, Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Curry Noodles",
    "iconKey": "Curry Noodles",
    "req_ingredients": "Noodles, Curry Powder",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Tempura Noodles",
    "iconKey": "Tempura Noodles",
    "req_ingredients": "Noodles, Tempura",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Fried Noodles",
    "iconKey": "Fried Noodles",
    "req_ingredients": "Noodles, any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Buckwheat Noodles",
    "iconKey": "Soba Noodles",
    "req_ingredients": "Buckwheat Flour",
    "req_utensils": "Pot, Knife, Rolling Pin",
    "req_seasoning": "-"
  },
  {
    "name": "Tempura Buckwheat Noodles",
    "iconKey": "Tempura Soba",
    "req_ingredients": "Tempura, Buckwheat Noodles",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Fried Buckwheat Noodles",
    "iconKey": "Fried Soba",
    "req_ingredients": "Buckwheat Noodles, any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "Salt, Vinegar, Soy Sauce"
  },
  {
    "name": "Buckwheat Chips",
    "iconKey": "Buckwheat Chips",
    "req_ingredients": "Buckwheat Flour",
    "req_utensils": "Pot, Rolling Pin",
    "req_seasoning": "-"
  },
  {
    "name": "Tempura",
    "iconKey": "Tempura",
    "req_ingredients": "Flour, any Egg, Oil",
    "req_utensils": "Frying Pan",
    "req_seasoning": "-"
  },
  {
    "name": "Mountain Stew",
    "iconKey": "Mountain Stew",
    "req_ingredients": "Carrot, Mushroom, Bamboo Shoot",
    "req_utensils": "Pot, Knife",
    "req_seasoning": "Sugar, Soy Sauce"
  },
  {
    "name": "Moon Dumpling",
    "iconKey": "Moon Dumplings",
    "req_ingredients": "Dumpling Powder",
    "req_utensils": "-",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Roasted Rice Cake",
    "iconKey": "Roasted Rice Cake",
    "req_ingredients": "Rice Cake",
    "req_utensils": "Oven",
    "req_seasoning": "Soy Sauce"
  },
  {
    "name": "Toasted Rice Ball",
    "iconKey": "Grilled Rice Ball",
    "req_ingredients": "Rice Ball",
    "req_utensils": "Oven",
    "req_seasoning": "Soy Sauce"
  },
  {
    "name": "Rice Gruel",
    "iconKey": "Rice Porridge",
    "req_ingredients": "Rice Ball",
    "req_utensils": "Pot",
    "req_seasoning": "Salt"
  },
  {
    "name": "Tempura Rice",
    "iconKey": "Tempura Rice",
    "req_ingredients": "Rice Ball, Tempura",
    "req_utensils": "-",
    "req_seasoning": "Salt"
  },
  {
    "name": "Egg Over Rice",
    "iconKey": "Egg over Rice",
    "req_ingredients": "Any Egg, Rice Ball",
    "req_utensils": "Pot",
    "req_seasoning": "Salt, Soy Sauce"
  },
  {
    "name": "Candied Potato",
    "iconKey": "Candied Sweet Potato",
    "req_ingredients": "Sweet Potato, Honey",
    "req_utensils": "Pot",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Potato Pancakes",
    "iconKey": "Potato Pancakes",
    "req_ingredients": "Potato, Onion, any Egg, Oil, Flour",
    "req_utensils": "Frying Pan, Knife",
    "req_seasoning": "Salt"
  },
  {
    "name": "Fish Sticks",
    "iconKey": "Fish Sticks",
    "req_ingredients": "Medium Fish",
    "req_utensils": "Mixer",
    "req_seasoning": "Salt"
  },
  {
    "name": "Cookies",
    "iconKey": "Cookies",
    "req_ingredients": "Flour, any Egg, Butter",
    "req_utensils": "Oven, Rolling Pin",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Chocolate Cookies",
    "iconKey": "Chocolate Cookies",
    "req_ingredients": "Flour, any Egg, Butter, Chocolate",
    "req_utensils": "Oven, Rolling Pin",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Ice Cream",
    "iconKey": "Ice Cream",
    "req_ingredients": "Any Milk, any Egg",
    "req_utensils": "Pot, Whisk",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Cake",
    "iconKey": "Cake",
    "req_ingredients": "Butter, Flour, Egg",
    "req_utensils": "Oven, Whisk",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Chocolate Cake",
    "iconKey": "Chocolate Cake",
    "req_ingredients": "Butter, Flour, any Egg, Chocolate",
    "req_utensils": "Oven, Whisk",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Pancakes",
    "iconKey": "Pancakes",
    "req_ingredients": "Flour, Oil, any Egg, any Milk, Honey, Butter",
    "req_utensils": "Frying Pan, Whisk",
    "req_seasoning": "Sugar"
  },
  {
    "name": "Relaxation Tea",
    "iconKey": "Relaxation Tea",
    "req_ingredients": "Relaxation Tea Leaves",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "SUGDW Apple",
    "iconKey": "SUGDW Apple",
    "req_ingredients": "Apple, HMSGB Apple, AEPFE Apple",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "HMSGB Apple",
    "iconKey": "HMSGB Apple",
    "req_ingredients": "Apple, SUGDW Apple, AEPFE Apple",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "AEPFE Apple",
    "iconKey": "AEPFE Apple",
    "req_ingredients": "Apple, SUGDW Apple, HMSGB Apple",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "Bodigizer",
    "iconKey": "Bodigizer",
    "req_ingredients": "Honey, Orange Grass, Black Grass, Red Magic Flower",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Bodigizer XL",
    "iconKey": "Bodigizer XL",
    "req_ingredients": "Bodigizer, Blue Grass",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Turbojolt",
    "iconKey": "Turbojolt",
    "req_ingredients": "Honey, Orange Grass, White Grass, Red Magic Flower",
    "req_utensils": "Pot",
    "req_seasoning": "-"
  },
  {
    "name": "Turbojolt XL",
    "iconKey": "Turbojolt XL",
    "req_ingredients": "Turbojolt, Green Grass",
    "req_utensils": "Mixer",
    "req_seasoning": "-"
  },
  {
    "name": "Relaxation Tea Leaves",
    "iconKey": "Relaxation Tea Leaves",
    "req_ingredients": "Red Grass, Orange Grass, Yellow Grass, Green Grass, Purple Grass, Blue Grass, Indigo Grass, Weed",
    "req_utensils": "Frying Pan, Knife",
    "req_seasoning": "-"
  },
  {
    "name": "Elli Leaves",
    "iconKey": "Elli Leaves",
    "req_ingredients": "Bodigizer XL, Turbojolt XL, all 6 burnt dishes",
    "req_utensils": "Frying Pan, Pot, Oven, Knife",
    "req_seasoning": "Sugar, Salt, Vinegar, Soy Sauce, Miso"
  },
  {
    "name": "The Spring Sun",
    "iconKey": "The Spring Sun",
    "req_ingredients": "Blue Magic Flower, Red Magic Flower, Moon Drop Flower, Toy Flower, Pink Cat Flower",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "The Summer Sun",
    "iconKey": "The Summer Sun",
    "req_ingredients": "All 3 fish sizes, Fossil of Ancient Fish, Pirate Treasure",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "The Autumn Sun",
    "iconKey": "The Autumn Sun",
    "req_ingredients": "Milk (X), Cheese (X), X Egg, Mayonnaise (X), Wool (X), Yarn (X)",
    "req_utensils": "-",
    "req_seasoning": "-"
  },
  {
    "name": "The Winter Sun",
    "iconKey": "The Winter Sun",
    "req_ingredients": "Alexandrite, Diamond, Pink Diamond, Emerald, Moonstone, Mythic Stone, Sand Rose",
    "req_utensils": "-",
    "req_seasoning": "-"
  }
];

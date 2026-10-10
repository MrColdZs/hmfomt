import json
import re
import difflib

with open('recipes_full.json') as f:
    recipes = json.load(f)

# The keys in ICONS_MAPPING are currently the items names like 'Mayonnaise S' 
# or Fandom names? In my previous script, I mapped 'Mayonnaise S' -> 'items_clean/recipe_mayonnaise_s.webp'
# But here `r.name` is the Fandom name, e.g., 'Mayonnaise (S)'.
# Let's map it back to the exact key in ICONS_MAPPING so the icons match!

items_text = open('index.html').read()
items_match = re.search(r'const ITEMS = \[([\s\S]*?)\];', items_text)
item_pairs = re.findall(r"\['([0-9A-F]+)','([^']+)'\]", items_match.group(1))
item_names = [p[1] for p in item_pairs]
food_items = [name for id_hex, name in item_pairs if (0x4C00 <= int(id_hex, 16) <= 0x9900) or (0xA300 <= int(id_hex, 16) <= 0xAA00) or name.endswith('Sun')]

mapped_recipes = []
used_food = set()

for r in recipes:
    fn = r['name'].replace('*', '').strip()
    
    manual = {
        'Mayonnaise (S)': 'Mayonnaise S',
        'Mayonnaise (M)': 'Mayonnaise M',
        'Mayonnaise (L)': 'Mayonnaise L',
        'Mayonnaise (G)': 'Mayonnaise G',
        'Mayonnaise (P)': 'Mayonnaise P',
        'Mayonnaise (X)': 'Mayonnaise X',
        'Milk (X)': 'Milk X',
        'Cheese (X)': 'Cheese X',
        'Wild Grape Juice': 'Grape Juice',
        'Stir Fry': 'Stir-Fried Vegetables',
        'Savory Pancake': 'Okonomiyaki',
        'Strawberry Milk': 'Strawberry Smoothie',
        'Tomato Juice': 'Tomato Juice',
        'Baked Corn': 'Roasted Corn',
        'Sweet Potatoes': 'Sweet Potato',
        'Baked Sweet Potato': 'Roasted Sweet Potato',
        'Greens': 'Green Vegetables',
        'Cheese Cake': 'Cheesecake',
        'Chirashi Sushi': 'Mixed Sashimi',
        'Buckwheat Noodles': 'Soba Noodles',
        'Tempura Buckwheat Noodles': 'Tempura Soba',
        'Fried Buckwheat Noodles': 'Fried Soba',
        'Moon Dumpling': 'Moon Dumplings',
        'Toasted Rice Ball': 'Grilled Rice Ball',
        'Rice Gruel': 'Rice Porridge',
        'Candied Potato': 'Candied Sweet Potato',
        'The Spring Sun': 'Spring Sun',
        'The Summer Sun': 'Summer Sun',
        'The Autumn Sun': 'Autumn Sun',
        'The Winter Sun': 'Winter Sun'
    }
    
    icon_key = fn
    if fn in manual and manual[fn] in item_names:
        icon_key = manual[fn]
    elif fn in item_names:
        icon_key = fn
    else:
        unmatched_food = [x for x in food_items if x not in used_food]
        close = difflib.get_close_matches(fn, unmatched_food, n=1, cutoff=0.5)
        if close:
            icon_key = close[0]
            used_food.add(close[0])

    # Let's write out the json
    mapped_recipes.append({
        'name': fn,
        'iconKey': icon_key,
        'req_ingredients': r['req_ingredients'] or '-',
        'req_utensils': r['req_utensils'] or '-',
        'req_seasoning': r['req_seasoning'] or '-'
    })

js_array = "const COOKING_RECIPES_DATA = " + json.dumps(mapped_recipes, indent=2) + ";\n"

with open('cooking_recipes_data.js', 'w') as f:
    f.write(js_array)

print("Generated COOKING_RECIPES_DATA")

import json
import difflib
import re

with open('recipes.json') as f:
    recipes = json.load(f)

items_text = open('index.html').read()
items_match = re.search(r'const ITEMS = \[([\s\S]*?)\];', items_text)
items_content = items_match.group(1)
item_pairs = re.findall(r"\['([0-9A-F]+)','([^']+)'\]", items_content)
item_names = [p[1] for p in item_pairs]
food_items = [name for id_hex, name in item_pairs if (0x4C00 <= int(id_hex, 16) <= 0x9900) or (0xA300 <= int(id_hex, 16) <= 0xAA00) or (0x2501 <= int(id_hex, 16) <= 0x2701) or name.endswith('Sun')]

mapping = {}

for r in recipes:
    fn = r['name'].replace('*', '').strip()
    safe_name = re.sub(r'[^a-zA-Z0-9_\- ]', '', fn).replace(' ', '_').lower()
    filename = f"items_clean/recipe_{safe_name}.webp"
    
    # Try exact match
    matches = [i for i in item_names if i.lower() == fn.lower()]
    if matches:
        mapping[matches[0]] = filename
        continue
    
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
    
    if fn in manual:
        if manual[fn] in item_names:
            mapping[manual[fn]] = filename
            continue
            
    # fuzzy match ONLY for unmatched item_names, to prevent overriding
    unmatched_food = [x for x in food_items if x not in mapping]
    close = difflib.get_close_matches(fn, unmatched_food, n=1, cutoff=0.5)
    if close:
        mapping[close[0]] = filename

print("  // Cooking Recipes (Fandom)")
for k, v in mapping.items():
    print(f"  '{k}': '{v}',")

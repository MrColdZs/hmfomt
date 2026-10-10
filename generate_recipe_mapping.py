import json
import re
import os

with open('recipes.json') as f:
    recipes = json.load(f)

# Create a map from recipe name to clean filename
mapping = {}
for r in recipes:
    name = r['name'].replace('*', '').strip()
    safe_name = re.sub(r'[^a-zA-Z0-9_\- ]', '', name).replace(' ', '_').lower()
    filename = f"recipe_{safe_name}.webp"
    mapping[name] = filename
    
    # We also map to standard names from the ITEMS array
    # because sometimes there's a slight mismatch (e.g. "Stir-Fried Vegetables" vs "Stir Fry")
    # Actually, let's just output this mapping to see.

# I will write the JS object string
print("  // Cooking Recipes")
for name, filename in mapping.items():
    print(f"  '{name}': 'items_clean/{filename}',")

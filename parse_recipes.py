import json
import re
import os

with open('fandom_recipes.json') as f:
    d = json.load(f)

html = d['parse']['text']['*']
# Find all <tr> tags
trs = re.findall(r'<tr.*?>(.*?)</tr>', html, flags=re.DOTALL | re.IGNORECASE)

recipes = []
for tr in trs:
    # First cell usually has the image and the name
    tds = re.findall(r'<td.*?>(.*?)</td>', tr, flags=re.DOTALL | re.IGNORECASE)
    if not tds:
        continue
    first_td = tds[0]
    
    # Extract image src or data-src
    img_match = re.search(r'<img[^>]+data-src="([^"]+)"', first_td)
    if img_match:
        img_url = img_match.group(1)
    else:
        img_match = re.search(r'<img[^>]+src="([^"]+)"', first_td)
        if img_match:
            img_url = img_match.group(1)
        else:
            continue
            
    # Extract name. It is after <br /> or we can use alt=""
    name_match = re.search(r'<br\s*/>\s*([^<]+)', first_td)
    if name_match:
        name = name_match.group(1).strip()
        recipes.append({"name": name, "url": img_url})

# Save to recipes.json
with open('recipes.json', 'w') as f:
    json.dump(recipes, f, indent=2)

print(f"Extracted {len(recipes)} recipes")

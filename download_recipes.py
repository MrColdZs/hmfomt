import json
import os
import subprocess
import urllib.parse
import re

with open('recipes.json') as f:
    recipes = json.load(f)

os.makedirs('items_clean', exist_ok=True)

downloaded = set()

for r in recipes:
    name = r['name'].replace('*', '').strip()
    url = r['url']
    
    # We can use the name as filename
    safe_name = re.sub(r'[^a-zA-Z0-9_\- ]', '', name).replace(' ', '_').lower()
    filename = f"recipe_{safe_name}.webp"
    filepath = os.path.join('items_clean', filename)
    
    if filepath not in downloaded and not os.path.exists(filepath):
        print(f"Downloading {name} from {url}")
        # Note: sometimes they are webp even with .png in the URL. We'll save them as .webp just in case,
        # but if they are png, the browser can handle it. Let's just name them .png actually, or .webp.
        # Fandom delivers webp by default. 
        cmd = ["curl", "-s", "-A", "Mozilla/5.0", url, "-o", filepath]
        subprocess.run(cmd)
        downloaded.add(filepath)

print("Done downloading recipes.")

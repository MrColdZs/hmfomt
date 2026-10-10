import urllib.request
import re
import os

url = "https://harvestmoon.fandom.com/wiki/Cooking_Recipes_(FoMT)"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all table rows
    rows = re.findall(r'<tr>(.*?)</tr>', html, re.DOTALL)
    
    if not os.path.exists('items_recipes'):
        os.makedirs('items_recipes')
        
    for row in rows:
        if 'data-src=' in row or 'src=' in row:
            # Extract image url
            img_match = re.search(r'src="(https://static.wikia.nocookie.net/harvestmoon/images/[^"]+)"', row)
            if not img_match:
                img_match = re.search(r'data-src="(https://static.wikia.nocookie.net/harvestmoon/images/[^"]+)"', row)
            
            # Extract name
            # Name is usually the first link after the image or in the next column
            name_match = re.search(r'title="([^"]+)"', row)
            if name_match and img_match:
                name = name_match.group(1).replace(' (FoMT)', '').strip()
                img_url = img_match.group(1).split('/revision/')[0]
                
                print(f"Found: {name} -> {img_url}")
                # clean name for filename
                safe_name = re.sub(r'[^a-zA-Z0-9_]', '', name.replace(' ', '_'))
                
                req2 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    img_data = urllib.request.urlopen(req2).read()
                    with open(f'items_recipes/{safe_name}.png', 'wb') as f:
                        f.write(img_data)
                except Exception as e:
                    print(f"Error downloading {img_url}: {e}")
                    
except Exception as e:
    print(e)

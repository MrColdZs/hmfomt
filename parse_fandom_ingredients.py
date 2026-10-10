import json
import re

with open('fandom_recipes.json') as f:
    d = json.load(f)

html = d['parse']['text']['*']
trs = re.findall(r'<tr.*?>(.*?)</tr>', html, flags=re.DOTALL | re.IGNORECASE)

recipes = []
for tr in trs:
    tds = re.findall(r'<td.*?>(.*?)</td>', tr, flags=re.DOTALL | re.IGNORECASE)
    if len(tds) >= 8:
        first_td = tds[0]
        # Extract name
        name_match = re.search(r'<br\s*/>\s*([^<]+)', first_td)
        if not name_match:
            continue
        name = name_match.group(1).replace('*', '').strip()
        
        def clean_tags(text):
            text = text.replace('<br />', ', ')
            text = text.replace('<br>', ', ')
            # remove all html tags
            text = re.sub(r'<[^>]+>', '', text)
            text = ' '.join(text.split())
            if text == 'None':
                return ''
            return text
            
        req_utensils = clean_tags(tds[1])
        req_seasoning = clean_tags(tds[3])
        req_ingredients = clean_tags(tds[5])
        
        opt_ingredients = clean_tags(tds[6])
        opt_utensils = clean_tags(tds[2])
        opt_seasoning = clean_tags(tds[4])
        
        desc = clean_tags(tds[7])
        
        # Combine required things
        reqs = []
        if req_utensils: reqs.append("Utensils: " + req_utensils)
        if req_seasoning: reqs.append("Seasoning: " + req_seasoning)
        if req_ingredients: reqs.append("Ingredients: " + req_ingredients)
        
        full_desc = " | ".join(reqs)
        if desc:
            full_desc += " — " + desc
            
        recipes.append({
            'name': name,
            'details': full_desc,
            'req_ingredients': req_ingredients,
            'req_utensils': req_utensils,
            'req_seasoning': req_seasoning
        })

with open('recipes_full.json', 'w') as f:
    json.dump(recipes, f, indent=2)

print(f"Parsed {len(recipes)} full recipes.")

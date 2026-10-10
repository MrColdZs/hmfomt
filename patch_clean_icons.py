import re

with open('index.html') as f:
    html = f.read()

replacements = [
    ('items/mine_alexandrite.gif', 'items_clean/mine_alexandrite.png'),
    ('items/mine_gold.gif', 'items_clean/mine_gold.png'),
    ('items/pirate_treasure.gif', 'items_clean/pirate_treasure.png'),
    ('items/sell_redmagicred.gif', 'items_clean/sell_redmagicred.png'),
    ('items/tool_wcan_sil.png', 'items_clean/tool_wcan_sil.png'),
    ('items/boy_tool5.png', 'items_clean/boy_tool5.png'),
    ('items/mine_sagestone.png', 'items_clean/mine_sagestone.png'),
    ('items/veg_corn.png', 'items_clean/veg_corn.png'),
    ('items/grass_green.png', 'items_clean/grass_green.png'),
    ('items/icon_dog.png', 'items_clean/icon_dog.png')
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)

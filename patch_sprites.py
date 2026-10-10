import re

with open('index.html') as f:
    html = f.read()

replacements = [
  ("'staid (sprite)': 'items/wool_sm.png'", "'staid (sprite)': 'items_clean/sprite_staid.webp'"),
  ("'nappy (sprite)': 'items/wool_sm.png'", "'nappy (sprite)': 'items_clean/sprite_nappy.webp'"),
  ("'bold (sprite)': 'items/wool_sm.png'", "'bold (sprite)': 'items_clean/sprite_bold.webp'"),
  ("'chef (sprite)': 'items/wool_sm.png'", "'chef (sprite)': 'items_clean/sprite_chef.webp'"),
  ("'aqua (sprite)': 'items/wool_sm.png'", "'aqua (sprite)': 'items_clean/sprite_aqua.webp'"),
  ("'hoggy (sprite)': 'items/wool_sm.png'", "'hoggy (sprite)': 'items_clean/sprite_hoggy.webp'"),
  ("'timid (sprite)': 'items/wool_sm.png'", "'timid (sprite)': 'items_clean/sprite_timid.webp'"),
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)

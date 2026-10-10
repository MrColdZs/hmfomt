import re

with open('index.html') as f:
    html = f.read()

replacements = [
  ("'heart level': 'items_clean/sell_redmagicred.png'", "'heart level': 'items_clean/red_heart.webp'"),
  ("'popuri': 'items/wool_sm.png'", "'popuri': 'items_clean/face_popuri.webp'"),
  ("'mary': 'items/wool_sm.png'", "'mary': 'items_clean/face_mary.webp'"),
  ("'karen': 'items/wool_sm.png'", "'karen': 'items_clean/face_karen.webp'"),
  ("'elli': 'items/wool_sm.png'", "'elli': 'items_clean/face_elli.webp'"),
  ("'ann': 'items/wool_sm.png'", "'ann': 'items_clean/face_ann.webp'"),
  ("'harvest goddess': 'items/wool_sm.png'", "'harvest goddess': 'items_clean/face_harvest_goddess.webp'")
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)

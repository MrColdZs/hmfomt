import re
import os

with open('index.html') as f:
    html = f.read()

# Get all items in items_clean
clean_files = set(os.listdir('items_clean'))

# Find all 'items/filename' in index.html
matches = re.findall(r"'items/([^']+)'", html)

replacements = {}
for m in matches:
    # m is e.g. "free_apple.gif"
    # the clean version is "free_apple.png" or "free_apple.webp" etc.
    clean_png = m.replace('.gif', '.png')
    if clean_png in clean_files:
        replacements[f"'items/{m}'"] = f"'items_clean/{clean_png}'"
    elif m in clean_files:
        replacements[f"'items/{m}'"] = f"'items_clean/{m}'"

for old, new in replacements.items():
    html = html.replace(old, new)
    print(f"Replaced {old} -> {new}")

with open('index.html', 'w') as f:
    f.write(html)
print("index.html patched with remaining icons!")

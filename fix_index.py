import re

with open('index.html') as f:
    html = f.read()

# Remove the old Cooking Recipes (Fandom) block
html = re.sub(
    r"  // Cooking Recipes \(Fandom\)\n(?:  '[^']+': '[^']+',\n)+",
    "",
    html
)

# Read the new snippet
with open('recipe_mapping_snippet.txt') as f:
    snippet = f.read()

# Insert the new snippet
html = re.sub(
    r"(const ICONS_MAPPING = \{)",
    r"\1\n" + snippet,
    html
)

with open('index.html', 'w') as f:
    f.write(html)

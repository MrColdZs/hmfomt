import re

with open('index.html') as f:
    html = f.read()

# 1. Update SECTIONS array
if "id: 'recipe'" not in html:
    recipe_section = """  {
    id: 'recipe', num: '09', title: 'Cooking Recipes', short: 'Recipes', accent: 'sun',
    lead: 'All 108 cooking recipes in the game. These can be spawned into your backpack just like regular items, or you can use them to win the Cooking Festival.',
    groups: [],
    ref: 'recipe'
  }"""
    html = re.sub(
        r"(ref: 'item'\n\s*}\n)\];",
        r"\1,\n" + recipe_section + "\n];",
        html
    )

# 2. Update render function
if "sec.ref === 'recipe'" not in html:
    recipe_render = """  if (sec.ref === 'recipe') {
    const recipesOnly = ITEMS.filter(x => {
       const v = parseInt(x[0], 16);
       return (v >= 0x4C00 && v <= 0x9900) || (v >= 0xA300 && v <= 0xAA00);
    });
    html += `<div class="mt-9">
      <h3 class="font-display font-extrabold text-lg mb-1">Cooking Recipes</h3>
      <p class="text-sm text-inksoft">Four-digit hexadecimal value for the <span class="font-mono text-[13px] font-bold">yyyy</span> field to spawn the dish in your first rucksack slot.</p>
      ${refTable('recipe-ref', recipesOnly, 'Recipe', v => `82004214 ${v}`)}
    </div>`;
  }"""
    html = html.replace("if (sec.ref === 'item') {", recipe_render + "\n\n  if (sec.ref === 'item') {")

# 3. Update counter loops
html = html.replace("['tool-ref', 'item-ref', 'day-ref']", "['tool-ref', 'item-ref', 'day-ref', 'recipe-ref']")
html = html.replace("{ 'tool-ref': 'tools', 'item-ref': 'items', 'day-ref': 'dates' }[id]", "{ 'tool-ref': 'tools', 'item-ref': 'items', 'day-ref': 'dates', 'recipe-ref': 'recipes' }[id]")

# 4. Insert recipe mapping to ICONS_MAPPING
with open('recipe_mapping_snippet.txt') as f:
    snippet = f.read()

if "Cooking Recipes (Fandom)" not in html:
    html = re.sub(
        r"(const ICONS_MAPPING = \{)",
        r"\1\n" + snippet,
        html
    )

with open('index.html', 'w') as f:
    f.write(html)
print("index.html patched!")

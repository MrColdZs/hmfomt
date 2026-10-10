import re

with open('index.html') as f:
    html = f.read()

with open('cooking_recipes_data.js') as f:
    recipe_data = f.read()

# 1. Inject COOKING_RECIPES_DATA before const SECTIONS =
if "COOKING_RECIPES_DATA" not in html:
    html = html.replace("const SECTIONS =", recipe_data + "\nconst SECTIONS =")

# 2. Add recipeTable function
recipe_table_func = """
  function recipeTable(id, recipes) {
    let out = `<div class="max-h-[22rem] overflow-y-auto mt-4 border-2 border-ink ref-scroll"><table class="reftable" id="${id}">`;
    out += `<thead><tr><th>Dish Name</th><th>Ingredients</th><th>Utensils</th><th>Seasoning</th></tr></thead><tbody class="font-mono text-sm">`;
    recipes.forEach(r => {
      const icon = ICONS_MAPPING[r.iconKey] || 'items/mine_pinkdiamond.gif';
      out += `<tr class="ref-row" data-name="${esc(r.name.toLowerCase())}">`;
      out += `<td><div class="flex items-center gap-3"><img src="${icon}" class="w-6 h-6 object-contain" style="image-rendering:pixelated"><span class="font-bold">${esc(r.name)}</span></div></td>`;
      out += `<td class="leading-snug text-xs sm:text-sm">${esc(r.req_ingredients)}</td>`;
      out += `<td class="leading-snug text-xs sm:text-sm">${esc(r.req_utensils)}</td>`;
      out += `<td class="leading-snug text-xs sm:text-sm">${esc(r.req_seasoning)}</td>`;
      out += `</tr>`;
    });
    out += `</tbody></table></div>`;
    out += `<p class="mt-2 text-[11px] font-mono font-bold tracking-wider text-inksoft text-right" id="${id}-count"></p>`;
    return out;
  }
"""
if "function recipeTable" not in html:
    html = html.replace("function refTable", recipe_table_func + "\n  function refTable")

# 3. Update the render section for recipe
old_recipe_render = """  if (sec.ref === 'recipe') {
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

new_recipe_render = """  if (sec.ref === 'recipe') {
    html += `<div class="mt-9">
      <h3 class="font-display font-extrabold text-lg mb-1">Cooking Recipes Guide</h3>
      <p class="text-sm text-inksoft">All the ingredients and utensils you need to cook every dish in your kitchen.</p>
      ${recipeTable('recipe-ref', COOKING_RECIPES_DATA)}
    </div>`;
  }"""

if old_recipe_render in html:
    html = html.replace(old_recipe_render, new_recipe_render)
else:
    # fallback with regex
    html = re.sub(r"if \(sec\.ref === 'recipe'\) \{.*?\n  \}", new_recipe_render, html, flags=re.DOTALL)


with open('index.html', 'w') as f:
    f.write(html)
print("index.html patched with new recipe table!")

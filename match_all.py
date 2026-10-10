from PIL import Image
import os
import json

def match(sheet_pix, sw, sh, template_path):
    try:
        template = Image.open(template_path).convert('RGBA')
    except:
        return -1, -1
    tw, th = template.size
    tpix = template.load()
    
    # optimize by only checking valid pixels
    valid_pixels = []
    for y in range(th):
        for x in range(tw):
            tr, tg, tb, ta = tpix[x, y]
            if ta > 0:
                valid_pixels.append((x, y, tr, tg, tb))
                
    if not valid_pixels: return -1, -1
    
    best_match = (-1, -1)
    best_score = float('inf')
    
    for y in range(sh - th):
        for x in range(sw - tw):
            score = 0
            valid = True
            for tx, ty, tr, tg, tb in valid_pixels:
                sr, sg, sb, sa = sheet_pix[x+tx, y+ty]
                if sa == 0:
                    score += 255 * 3
                else:
                    score += abs(tr - sr) + abs(tg - sg) + abs(tb - sb)
                if score > best_score:
                    valid = False
                    break
            
            if valid and score < best_score:
                best_score = score
                best_match = (x, y)
                if best_score == 0:
                    return best_match # perfect match
                
    return best_match

files = ['mine_alexandrite.gif', 'mine_gold.gif', 'pirate_treasure.gif', 'sell_redmagicred.gif', 'tool_wcan_sil.png', 'boy_tool5.png', 'mine_sagestone.png', 'veg_corn.png', 'grass_green.png', 'icon_dog.png', 'icon_horse.png', 'icon_chickens.png', 'icon_cow.png', 'house_villa.png', 'house_farm.png', 'house_beach.png', 'wool_sm.png', 'free_apple.gif', 'grass_yellow.png', 'grass_blue.png']

sheet = Image.open('sheet_transparent.png').convert('RGBA')
sw, sh = sheet.size
spix = sheet.load()

results = {}
for f in files:
    x, y = match(spix, sw, sh, 'items/' + f)
    print(f"{f}: {x}, {y}")
    if x != -1:
        # Save a clean 16x16 crop!
        # wait, the item size is template size, but actually let's just crop 16x16
        # some might be 24x24
        template = Image.open('items/' + f)
        tw, th = template.size
        crop = sheet.crop((x, y, x+tw, y+th))
        crop.save('items_clean/' + f.replace('.gif', '.png'))


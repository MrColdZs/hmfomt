from PIL import Image

def match(sheet_path, template_path):
    sheet = Image.open(sheet_path).convert('RGBA')
    template = Image.open(template_path).convert('RGBA')
    
    sw, sh = sheet.size
    tw, th = template.size
    
    spix = sheet.load()
    tpix = template.load()
    
    best_match = None
    best_score = float('inf')
    
    for y in range(sh - th):
        for x in range(sw - tw):
            score = 0
            valid = True
            for ty in range(th):
                for tx in range(tw):
                    tr, tg, tb, ta = tpix[tx, ty]
                    if ta == 0: continue # ignore transparent template pixels
                    
                    sr, sg, sb, sa = spix[x+tx, y+ty]
                    if sa == 0:
                        score += 255 * 3 # penalty
                    else:
                        score += abs(tr - sr) + abs(tg - sg) + abs(tb - sb)
                        
                    if score > best_score:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid and score < best_score:
                best_score = score
                best_match = (x, y)
                
    return best_match, best_score

print(match('sheet_transparent.png', 'items/mine_gold.gif'))
print(match('sheet_transparent.png', 'items/pirate_treasure.gif'))

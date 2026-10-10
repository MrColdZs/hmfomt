import json
import os
import multiprocessing
from PIL import Image

def match(args):
    f, sheet_path = args
    template_path = os.path.join('items', f)
    try:
        template = Image.open(template_path).convert('RGBA')
    except:
        return f, -1, -1
        
    sheet = Image.open(sheet_path).convert('RGBA')
    sw, sh = sheet.size
    spix = sheet.load()
    
    tw, th = template.size
    tpix = template.load()
    
    valid_pixels = []
    for y in range(th):
        for x in range(tw):
            tr, tg, tb, ta = tpix[x, y]
            if ta > 0:
                valid_pixels.append((x, y, tr, tg, tb))
                
    if not valid_pixels: return f, -1, -1
    
    best_match = (-1, -1)
    best_score = float('inf')
    
    for y in range(sh - th):
        for x in range(sw - tw):
            score = 0
            valid = True
            for tx, ty, tr, tg, tb in valid_pixels:
                sr, sg, sb, sa = spix[x+tx, y+ty]
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
                    break
        if best_score == 0:
            break
            
    return f, best_match[0], best_match[1]

if __name__ == '__main__':
    with open('files_list.txt') as f:
        files = [line.strip() for line in f.read().split(',') if line.strip()]
        
    sheet_path = 'sheet_transparent.png'
    
    args = [(f, sheet_path) for f in files]
    
    with multiprocessing.Pool(processes=4) as pool:
        for f, x, y in pool.imap_unordered(match, args):
            print(f"{f}: {x}, {y}", flush=True)
            if x != -1:
                sheet = Image.open(sheet_path).convert('RGBA')
                template = Image.open(os.path.join('items', f))
                tw, th = template.size
                crop = sheet.crop((x, y, x+tw, y+th))
                crop.save('items_clean/' + f.replace('.gif', '.png'))


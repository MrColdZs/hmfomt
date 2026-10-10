from PIL import Image, ImageDraw
import sys

img = Image.open('sheet.png').convert('RGBA')
bg_color = img.getpixel((0,0))
pixels = img.load()

# Make bg transparent
for y in range(img.height):
    for x in range(img.width):
        if pixels[x,y][:3] == bg_color[:3]:
            pixels[x,y] = (0, 0, 0, 0)

img.save('sheet_transparent.png')

import cv2
import numpy as np
import os

if not os.path.exists('extracted'):
    os.makedirs('extracted')

cv_img = cv2.imread('sheet_transparent.png', cv2.IMREAD_UNCHANGED)
alpha_channel = cv_img[:, :, 3]
_, thresh = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

html = "<html><body style='background:#333;color:white;font-family:sans-serif;'><div style='display:flex;flex-wrap:wrap;'>"
idx = 0
for i, c in enumerate(contours):
    x, y, w, h = cv2.boundingRect(c)
    if w >= 8 and h >= 8 and w <= 64 and h <= 64:
        # crop
        crop = img.crop((x, y, x+w, y+h))
        crop.save(f'extracted/icon_{idx}.png')
        html += f"<div style='margin:10px;text-align:center;'><img src='extracted/icon_{idx}.png' style='width:32px;image-rendering:pixelated;'><br>{idx}</div>"
        idx += 1

html += "</div></body></html>"
with open('icons.html', 'w') as f:
    f.write(html)

print(f"Extracted {idx} icons.")

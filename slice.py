from PIL import Image
import os

img = Image.open('sheet_transparent.png')
w, h = img.size

if not os.path.exists('extracted'):
    os.makedirs('extracted')

html = "<html><body style='background:#333;color:white;font-family:sans-serif;'><div style='display:flex;flex-wrap:wrap;'>"

# just assume a grid size, say 16x16, let's just make a huge html table of the image so they can hover
html = """
<html>
<head>
<style>
  body { background: #333; }
  .grid { display: grid; grid-template-columns: repeat(30, 16px); gap: 1px; }
  .cell { width: 16px; height: 16px; background-image: url('sheet_transparent.png'); position: relative; }
  .cell:hover::after { content: attr(title); position: absolute; z-index: 10; background: black; color: white; top: -20px; left: 0; white-space: nowrap; font-size: 10px; }
</style>
</head>
<body>
<div class="grid">
"""

cols = w // 17
rows = h // 17
# wait, I don't know the grid size. Maybe I should just write a custom JS picker tool?

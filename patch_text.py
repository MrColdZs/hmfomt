import re

with open('index.html') as f:
    html = f.read()

# 1. Simplify the warning text
old_warning = """<p class="font-mono text-[10px] font-bold tracking-wider text-ink/70 mb-3">FROM THE ARCHIVE'S MASCOT</p>
      <p class="font-display font-extrabold text-xl leading-snug mb-3 max-w-[42ch]">
        Copy your save file before you switch any of this on.
      </p>
      <p class="text-sm text-ink/80 leading-relaxed max-w-[58ch] mb-6">
        These codes write straight into memory while the game is running, and a bad write can leave a save in a strange state. One copy of the <span class="font-mono text-[13px] font-bold">.sav</span> file beforehand and you can experiment without ever losing a farm.
      </p>"""

new_warning = """<p class="font-mono text-[10px] font-bold tracking-wider text-ink/70 mb-3">A QUICK WARNING</p>
      <p class="font-display font-extrabold text-xl leading-snug mb-3 max-w-[42ch]">
        Backup your save file first.
      </p>
      <p class="text-sm text-ink/80 leading-relaxed max-w-[58ch] mb-6">
        Cheats modify memory directly. Keep a copy of your <span class="font-mono text-[13px] font-bold">.sav</span> file to avoid losing your farm if something goes wrong.
      </p>"""

if old_warning in html:
    html = html.replace(old_warning, new_warning)
else:
    print("Warning text not found! (Maybe spacing is different?)")
    # fallback with regex
    html = re.sub(r"<p class=\"font-mono[^>]+>FROM THE ARCHIVE'S MASCOT</p>\s*<p[^>]+>\s*Copy your save file before you switch any of this on.\s*</p>\s*<p[^>]+>\s*These codes write straight into memory.*?</p>", new_warning, html, flags=re.DOTALL)

# 2. Add something below Natsume logo in the mascot section
old_logo_section = """    <div class="shrink-0 self-center sm:self-start">
      <picture>
        <source srcset="items/natsume_logo.svg" type="image/svg+xml">
        <img src="items/natsume_logo.svg" width="400" height="361" loading="lazy" decoding="async"
             alt="Three cartoon chickens: two adults with red combs and a small yellow chick"
             class="w-40 sm:w-48 h-auto">
      </picture>
    </div>"""

new_logo_section = """    <div class="shrink-0 self-center sm:self-start flex flex-col items-center">
      <picture>
        <source srcset="items/natsume_logo.svg" type="image/svg+xml">
        <img src="items/natsume_logo.svg" width="400" height="361" loading="lazy" decoding="async"
             alt="Natsume Logo"
             class="w-40 sm:w-48 h-auto">
      </picture>
      <p class="mt-4 font-mono text-[10px] font-bold tracking-widest text-ink/70 bg-paper2 px-3 py-1 border-2 border-ink/20 rounded-full">"SERIOUS FUN!"</p>
    </div>"""

if old_logo_section in html:
    html = html.replace(old_logo_section, new_logo_section)
else:
    print("Logo section not found! Will try regex.")
    html = re.sub(r'(<div class="shrink-0 self-center sm:self-start">.*?<picture>.*?</picture>)\s*(</div>)', r'\1\n      <p class="mt-4 font-mono text-[10px] font-bold tracking-widest text-ink/70 bg-paper2 px-3 py-1 border-2 border-ink/20 rounded-full text-center">"SERIOUS FUN!"</p>\n\2', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("index.html text patched!")

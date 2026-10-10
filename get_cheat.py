import urllib.request
import re
url = "https://www.neoseeker.com/harvest-moon-fomt/action_replay/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    print("Found AR codes. Searching for recipes...")
    recipes = re.findall(r'.{0,50}recipe.{0,100}', html, flags=re.IGNORECASE|re.DOTALL)
    for r in recipes[:10]:
        print(r)
except:
    pass

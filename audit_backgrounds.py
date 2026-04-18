import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

all_bg = set()
for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        all_bg.update(re.findall(r'data-bg-image="([^"]*)"', content))

print("Unique data-bg-image values found:")
for bg in sorted(list(all_bg)):
    print(f"  - {bg}")

import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Reverting footer background to original template asset
footer_bg_original = './assets/images/footer/h1-footer-bg.png'

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target the specific footer background replacement
    new_content = re.sub(r'data-bg-image="https://images\.unsplash\.com/photo-1451187580459-43490279c0fa[^"]*"', f'data-bg-image="{footer_bg_original}"', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Footer background reverted to original template asset site-wide.")

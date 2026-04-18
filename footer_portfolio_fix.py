import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Footer "Our Portfolio" links
    # Replace <a href="portfolios.html">Our Portfolio</a> with <a href="operational-excellence.html">Our Portfolio</a>
    content = content.replace('href="portfolios.html"', 'href="operational-excellence.html"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer links updated to point to a specific portfolio page.")

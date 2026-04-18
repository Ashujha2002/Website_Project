import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We want to replace the whole "Pages" dropdown block with just a single "About Us" link.
# Target block:
# <li class="has-dropdown[^"]*"><a href="#">Pages</a>
#   <ul class="sub-menu">
#     ...
#   </ul>
# </li>

for filename in all_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Regex to find the "Pages" dropdown block
    # We'll use a non-greedy match for the ul content
    pages_dropdown_pattern = r'<li class="has-dropdown[^"]*"><a href="#">Pages</a>\s*<ul class="sub-menu">.*?</ul>\s*</li>'
    
    # Replacement depends on if we are on about.html (active state)
    if filename == 'about.html':
        replacement = '<li class="current-menu-item"><a href="about.html">About Us</a></li>'
    else:
        replacement = '<li><a href="about.html">About Us</a></li>'
        
    content = re.sub(pages_dropdown_pattern, replacement, content, flags=re.DOTALL)
    
    # 2. Also check for cases where "Pages" might be in a different format (e.g. current-menu-ancestor)
    # The regex above handles [^"]* so it should cover current-menu-ancestor too.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation updated: 'Pages' dropdown replaced with direct 'About Us' link site-wide.")

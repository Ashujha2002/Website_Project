import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in all_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the entire pxn_header_contact div (Sticky and Regular)
    # <div class="pxn_header_contact[^"]*">.*?</div>
    content = re.sub(r'<div class="pxn_header_contact[^"]*">.*?</div>', '', content, flags=re.DOTALL)
    
    # 2. Also remove any remaining contact_no or cta_action links with the NIF (except on contact.html main sections)
    if filename != 'contact.html':
        content = re.sub(r'<a[^>]*class="[^"]*(contact_no|cta_action)[^"]*"[^>]*>B95533089</a>', '', content)
    
    # 3. Clean up the offcanvas contact area where NIF might still be
    # <div class="offcanvas_contact pxn_contact"> ... B95533089 ... </div>
    # But only the one containing B95533089
    content = re.sub(r'<div class="offcanvas_contact pxn_contact">\s*<div class="contact_title">Contact</div>\s*<a[^>]*>B95533089</a>', 
                     '<div class="offcanvas_contact pxn_contact"><div class="contact_title">Contact</div>', content, flags=re.DOTALL)
    
    # Actually, simpler:
    content = content.replace('<a href="contact.html" class="contact_info">B95533089</a>', '')
    content = content.replace('<a href="contact.html" class="contact_no">B95533089</a>', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Aggressive NIF removal from navigation bars complete.")

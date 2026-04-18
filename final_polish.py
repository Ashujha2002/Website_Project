import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'

# 1. Image URL Mapping for better reliability
# Using shorter, more standard Unsplash URLs
img_updates = {
    "strategic-planning.html": {
        "main": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1200"
    },
    "digital-transformation.html": {
        "main": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200"
    },
    "risk-management.html": {
        "main": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&q=80&w=1200"
    },
    "business-process.html": {
        "main": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&q=80&w=1200"
    },
    "financial-management.html": {
        "main": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1554224155-169745fe9a5c?auto=format&fit=crop&q=80&w=1200"
    },
    "market-research.html": {
        "main": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1551288049-bbbda536339a?auto=format&fit=crop&q=80&w=1200"
    },
    "business-optimization.html": {
        "main": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&q=80&w=1200"
    },
    "it-consulting.html": {
        "main": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=1200"
    },
    "change-management.html": {
        "main": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&q=80&w=1200"
    },
    "leadership.html": {
        "main": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&q=80&w=1200"
    },
    "growth-expansion.html": {
        "main": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1200",
        "second": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1200"
    }
}

all_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in all_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. Update Footer Slider Text
    # Replace "call for project B95533089" with "Connect us at office@abentis.es"
    content = content.replace("call for project B95533089", "Connect us at office@abentis.es")
    
    # 3. Remove Phone Icon and NIF from Nav/Offcanvas (EXCEPT contact.html for the main NIF section)
    # The user wants it removed from "nav bar of every page"
    # We will remove the small NIF links in offcanvas and headers
    
    # Remove <a href="contact.html" class="contact_info">B95533089</a>
    content = re.sub(r'<a href="contact\.html" class="contact_info">B95533089</a>', '', content)
    
    # Remove pxni-phone icons (everywhere except contact.html)
    if filename != 'contact.html':
        content = content.replace('<i class="pxni-phone"></i>', '')
        # Also remove any surrounding divs if they were just for the phone
        # <div class="pxn_topbar_info"><i class="pxni-phone"></i>...</div>
        content = re.sub(r'<div class="pxn_topbar_info">\s*<i class="pxni-phone"></i>.*?</div>', '', content, flags=re.DOTALL)

    # 4. Update Images for Service Pages
    if filename in img_updates:
        # Replace main image
        # The main image is inside col-12 col-md-6 col-lg-12 col-xl-6
        # We'll search for the current unsplash URL and replace it
        content = re.sub(r'src="https://images\.unsplash\.com/[^"]*photo-1552664730-d307ca884978[^"]*"', f'src="{img_updates[filename]["main"]}"', content)
        # Handle cases where it was a different Unsplash URL or a broken one
        # Actually, let's just replace all Unsplash images in the service content with the correct ones
        # But only in the main content area.
        # It's safer to just replace the ones we know
        
        # Generic Unsplash Replacement for the first two images in service pages
        matches = re.findall(r'src="(https://images\.unsplash\.com/[^"]*)"', content)
        if len(matches) >= 2:
            content = content.replace(matches[0], img_updates[filename]["main"])
            content = content.replace(matches[1], img_updates[filename]["second"])

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer slider updated, Nav icons/NIF removed, and Images optimized site-wide.")

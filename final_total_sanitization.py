import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

portfolio_pages = [
    "operational-excellence.html",
    "market-expansion.html",
    "financial-restructuring.html",
    "tech-integration.html"
]

# Robust Unsplash Images for various sections
img_map = {
    # Page Headers
    r'data-bg-image="\./assets/images/page-header/page-header-bg\.jpg"': 'data-bg-image="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80"',
    # Projects on Home/About
    r'src="\./assets/images/projects/h1-project-img-1\.jpg"': 'src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80"',
    r'src="\./assets/images/projects/h1-project-img-2\.jpg"': 'src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"',
    r'src="\./assets/images/projects/h1-project-img-4\.jpg"': 'src="https://images.unsplash.com/photo-1554224155-169745fe9a5c?auto=format&fit=crop&w=800&q=80"',
    r'src="\./assets/images/projects/h1-project-img-3\.jpg"': 'src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80"',
    # Sidebars
    r'data-bg-image="\./assets/images/projects/sidebar-cta-bg\.jpg"': 'data-bg-image="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80"',
}

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace service-details.html
    content = content.replace('service-details.html', 'strategic-planning.html')
    
    # 2. Replace portfolio-details.html (Rotation)
    class Counter:
        def __init__(self):
            self.count = 0
        def get_next(self, match):
            p = portfolio_pages[self.count % len(portfolio_pages)]
            self.count += 1
            return f'href="{p}"'
    
    cnt = Counter()
    content = re.sub(r'href="portfolio-details\.html"', cnt.get_next, content)

    # 3. Global Image Fixes
    for pattern, replacement in img_map.items():
        content = re.sub(pattern, replacement, content)
    
    # Also handle some generic broken images in details pages
    content = content.replace('src="./assets/images/projects/project-details-img-1.jpg"', 'src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1200&q=80"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final link and image sanitization complete site-wide.")

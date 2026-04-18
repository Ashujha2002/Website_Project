import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'

# Portfolio Pages
portfolios = [
    'operational-excellence.html',
    'market-expansion.html',
    'financial-restructuring.html',
    'tech-integration.html'
]

# Blog Pages
blogs = [
    'strategic-growth-insights.html',
    'digital-transformation-trends.html',
    'efficient-operations-guide.html'
]

# Service Pages
services = [
    'strategic-planning.html',
    'digital-transformation.html',
    'risk-management.html',
    'business-process.html',
    'financial-management.html',
    'market-research.html',
    'business-optimization.html',
    'it-consulting.html',
    'change-management.html',
    'leadership.html',
    'growth-expansion.html'
]

def get_nav_html(prev_page, next_page):
    return f'''
                  <!-- navigation -->
                  <div class="pxn_post_navigation">
                    <a href="{prev_page}" class="navigation prev">
                      <span class="navigation_icon"><i class="pxni-arrow-left-2"></i></span>
                      <span class="navigation_text">Previous</span>
                    </a>

                    <a href="{next_page}" class="navigation next">
                      <span class="navigation_text">Next</span>
                      <span class="navigation_icon"><i class="pxni-arrow-right-2"></i></span>
                    </a>
                  </div>
'''

# 1. Update Portfolio and Blog circular navigation (already done but safe to repeat)
def update_circular_nav(pages):
    for i, page in enumerate(pages):
        filepath = os.path.join(directory, page)
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
        prev_p = pages[(i - 1) % len(pages)]
        next_p = pages[(i + 1) % len(pages)]
        content = re.sub(r'<div class="pxn_post_navigation">.*?</div>', get_nav_html(prev_p, next_p).strip(), content, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f: f.write(content)

update_circular_nav(portfolios)
update_circular_nav(blogs)

# 2. Add navigation to Services and fix their sidebars
for i, page in enumerate(services):
    filepath = os.path.join(directory, page)
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    
    # Add circular nav if missing
    if 'pxn_post_navigation' not in content:
        # Insert before <!-- sidebar --> or end of pxn_service_content
        nav_block = get_nav_html(services[(i-1)%len(services)], services[(i+1)%len(services)])
        content = content.replace('<!-- sidebar -->', nav_block + '\n              <!-- sidebar -->')
    else:
        # Update existing
        prev_p = services[(i-1)%len(services)]
        next_p = services[(i+1)%len(services)]
        content = re.sub(r'<div class="pxn_post_navigation">.*?</div>', get_nav_html(prev_p, next_p).strip(), content, flags=re.DOTALL)

    # Fix Sidebar Links (Exclusive Services)
    # We want to map them to the real pages
    service_mapping = {
        "Strategic Planning": "strategic-planning.html",
        "Business Optimization": "business-optimization.html",
        "IT Consulting": "it-consulting.html",
        "Change Management": "change-management.html",
        "Leadership": "leadership.html",
        "Digital Transformation": "digital-transformation.html",
        "Risk Management": "risk-management.html",
        "Business Process": "business-process.html",
        "Financial Management": "financial-management.html",
        "Market Research": "market-research.html",
        "Growth & Expansion": "growth-expansion.html"
    }
    
    for title, link in service_mapping.items():
        # Match <a class="service..." href="..."> <span class="service_title">TITLE</span>
        pattern = fr'(<a class="service[^"]*" href=")[^"]*(">.*?<span class="service_title">{re.escape(title)}</span>)'
        content = re.sub(pattern, rf'\1{link}\2', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f: f.write(content)

print("Site-wide navigation and sidebar links have been synchronized and repaired.")

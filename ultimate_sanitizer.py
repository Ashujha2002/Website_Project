import os
import re

# Reliable Pexels Images
HERO_IMAGES = [
    "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1920&q=80",
    "https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1920&q=80"
]
BUSINESS_IMAGE = "https://images.pexels.com/photos/3183181/pexels-photo-3183181.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

# Pages
services = [
    ('it-consulting.html', 'IT Consulting'),
    ('strategic-planning.html', 'Strategic Planning'),
    ('operational-excellence.html', 'Operational Excellence'),
    ('financial-management.html', 'Financial Management'),
    ('market-research.html', 'Market Research'),
    ('risk-management.html', 'Risk Management'),
    ('digital-transformation.html', 'Digital Transformation'),
    ('business-process.html', 'Business Process Improvement'),
    ('change-management.html', 'Change Management'),
    ('leadership.html', 'Leadership Development'),
    ('growth-expansion.html', 'Growth & Expansion')
]

portfolio_pages = [
    'operational-excellence.html',
    'market-expansion.html',
    'financial-restructuring.html',
    'tech-integration.html'
]

blog_pages = [
    'strategic-growth-insights.html',
    'digital-transformation-trends.html',
    'efficient-operations-guide.html'
]

def get_block(content, start_marker, end_marker):
    start = content.find(start_marker)
    end = content.find(end_marker, start)
    if start != -1 and end != -1:
        return content[start:end + len(end_marker)]
    return None

# 1. Get Definitive Blocks from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Using start/end comments as markers
OFFCANVAS = get_block(index_content, '<!-- start: Offcanvas -->', '<!-- end: Offcanvas -->')
HEADER = get_block(index_content, '<!-- start: Header Area -->', '</header>\n\n  <header class="pxn-header header-duplicate header-1 header-sticky">')
HEADER_DUPLICATE = get_block(index_content, '<header class="pxn-header header-duplicate header-1 header-sticky">', '</header>')
FOOTER = get_block(index_content, '<!-- start: Footer -->', '<!-- end: Footer -->')
SCRIPTS = get_block(index_content, '<!-- JS here -->', '</html>')

def sanitize_page(filepath):
    print(f"Sanitizing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply Blocks
    if OFFCANVAS: content = re.sub(r'<!-- start: Offcanvas -->.*?<!-- end: Offcanvas -->', OFFCANVAS, content, flags=re.DOTALL)
    if HEADER: content = re.sub(r'<!-- start: Header Area -->.*?<header class="pxn-header header-duplicate header-1 header-sticky">', HEADER, content, flags=re.DOTALL)
    if HEADER_DUPLICATE: content = re.sub(r'<header class="pxn-header header-duplicate header-1 header-sticky">.*?</header>', HEADER_DUPLICATE, content, flags=re.DOTALL)
    if FOOTER: content = re.sub(r'<!-- start: Footer -->.*?<!-- end: Footer -->', FOOTER, content, flags=re.DOTALL)
    if SCRIPTS: content = re.sub(r'<!-- JS here -->.*', SCRIPTS, content, flags=re.DOTALL)

    # Rebrand
    content = content.replace('Rovix', 'ABENTIS CONSULTING SL')
    
    # Fix Images (Replace all Unsplash with a reliable fallback if it's not the hero)
    content = re.sub(r'https://images\.unsplash\.com/photo-[^"\']+', BUSINESS_IMAGE, content)
    
    # Fix Sidebar for Service Pages
    if filepath in [s[0] for s in services]:
        sidebar_html = '<ul class="pxn_services_list">\n'
        for s_file, s_name in services:
            active_class = "active" if s_file == filepath else ""
            sidebar_html += f'                      <li>\n                        <a class="service {active_class}" href="{s_file}">\n                          <span class="service_title">{s_name}</span>\n                          <span class="service_icon">\n                            <span>\n                              <i class="pxni-arrow-right"></i>\n                              <i class="pxni-arrow-right"></i>\n                            </span>\n                          </span>\n                        </a>\n                      </li>\n'
        sidebar_html += '                    </ul>'
        content = re.sub(r'<ul class="pxn_services_list">.*?</ul>', sidebar_html, content, flags=re.DOTALL)

    # Fix Portfolio List Page
    if filepath == 'portfolios.html':
        # Re-map projects in order
        proj_mappings = [
            ('operational-excellence.html', 'Operational Excellence'),
            ('market-expansion.html', 'Market Expansion'),
            ('financial-restructuring.html', 'Financial Restructuring'),
            ('tech-integration.html', 'Tech Integration'),
            ('operational-excellence.html', 'Operational Excellence'), # Repeat for filler if needed
            ('market-expansion.html', 'Market Expansion')
        ]
        # This is very specific to the structure I saw
        items = re.findall(r'<div class="pxn-h3_project_item">.*?</div>\s*</div>\s*</div>', content, flags=re.DOTALL)
        new_items = []
        for i, item in enumerate(items):
            if i < len(proj_mappings):
                p_file, p_name = proj_mappings[i]
                item = re.sub(r'href="[^"]*"', f'href="{p_file}"', item)
                item = re.sub(r'>(.*?)</a>', f'>{p_name}</a>', item, count=1) # Fix first link (image?)
                # Actually, let's just use a more robust replacement for the item
                item = f'''<div class="pxn-h3_project_item">
                      <div class="project_img">
                        <a href="{p_file}">
                          <img src="{BUSINESS_IMAGE}" alt="Project"></a>

                        <div class="project_content">
                          <div class="project_cat">
                            <a class="category" href="#">Strategy</a>,
                            <a class="category" href="#">Growth</a>
                          </div>
                          <h3 class="project_title">
                            <a href="{p_file}">{p_name}</a>
                          </h3>
                        </div>
                      </div>
                    </div>'''
                new_items.append(item)
        content = re.sub(r'<div class="pxn_page_projects">.*?</div>\s*</div>\s*</div>\s*</div>', '<div class="pxn_page_projects">\n' + '\n'.join(new_items) + '\n</div>', content, flags=re.DOTALL)

    # Circular Navigation
    filename = os.path.basename(filepath)
    prev_link, next_link = None, None
    if filename in portfolio_pages:
        idx = portfolio_pages.index(filename)
        prev_link = portfolio_pages[(idx - 1) % len(portfolio_pages)]
        next_link = portfolio_pages[(idx + 1) % len(portfolio_pages)]
    elif filename in [s[0] for s in services]:
        s_list = [s[0] for s in services]
        idx = s_list.index(filename)
        prev_link = s_list[(idx - 1) % len(s_list)]
        next_link = s_list[(idx + 1) % len(s_list)]
    elif filename in blog_pages:
        idx = blog_pages.index(filename)
        prev_link = blog_pages[(idx - 1) % len(blog_pages)]
        next_link = blog_pages[(idx + 1) % len(blog_pages)]

    if prev_link and next_link:
        new_nav = f'''<!-- navigation -->
                  <div class="pxn_post_navigation">
                    <a href="{prev_link}" class="navigation prev">
                      <span class="navigation_icon"><i class="pxni-arrow-left-2"></i></span>
                      <span class="navigation_text">Previous</span>
                    </a>

                    <a href="{next_link}" class="navigation next">
                      <span class="navigation_text">Next</span>
                      <span class="navigation_icon"><i class="pxni-arrow-right-2"></i></span>
                    </a>
                  </div>'''
        if '<div class="pxn_post_navigation">' in content:
            content = re.sub(r'(<!-- navigation -->\s*)?<div class="pxn_post_navigation">.*?</div>', new_nav, content, flags=re.DOTALL)
        else:
            content = content.replace('<!-- end: Post Content -->', '<!-- end: Post Content -->\n                  ' + new_nav)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Run for all files
all_html = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
for f in all_html:
    sanitize_page(f)

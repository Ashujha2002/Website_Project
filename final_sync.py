import os
import re

# Navigation mappings
portfolio_pages = [
    'operational-excellence.html',
    'market-expansion.html',
    'financial-restructuring.html',
    'tech-integration.html'
]

service_pages = [
    'it-consulting.html',
    'strategic-planning.html',
    'operational-excellence-service.html', # Wait, operational-excellence is both portfolio and service? 
    # Let me check service list in index.html
]

# Looking at index.html service section (I remember it was 11 items)
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

portfolio_items = [
    ('operational-excellence.html', 'Operational Excellence'),
    ('market-expansion.html', 'Market Expansion'),
    ('financial-restructuring.html', 'Financial Restructuring'),
    ('tech-integration.html', 'Tech Integration')
]

blog_pages = [
    'strategic-growth-insights.html',
    'digital-transformation-trends.html',
    'efficient-operations-guide.html'
]

# Reliable Pexels Images
HERO_IMAGES = [
    "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1920&q=80",
    "https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1920&q=80"
]

SERVICE_IMAGE = "https://images.pexels.com/photos/3183181/pexels-photo-3183181.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
PORTFOLIO_IMAGE = "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Hero Backgrounds (for index.html mostly)
    if 'index.html' in filepath:
        content = content.replace('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80', HERO_IMAGES[0])
        content = content.replace('https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1920&q=80', HERO_IMAGES[1])

    # 2. Fix Broken Detail Images (replace all Unsplash that might be failing)
    content = re.sub(r'https://images\.unsplash\.com/photo-[^"\']+', PORTFOLIO_IMAGE, content)
    
    # 3. Fix Portfolio List Page (portfolios.html)
    if 'portfolios.html' in filepath or 'index.html' in filepath:
        # Map titles to pages
        mappings = {
            'Business Analytics & Reporting': 'tech-integration.html',
            'Sales and Marketing Strategy': 'market-expansion.html',
            'Business Process Optimization': 'operational-excellence.html',
            'Financial Planning & Forecasting': 'financial-restructuring.html'
        }
        for title, page in mappings.items():
            # Use regex to find the title and update the preceding href
            # Pattern: <a href="[^"]*">Title</a>
            content = re.sub(f'<a href="[^"]*">({re.escape(title)})</a>', f'<a href="{page}">\\1</a>', content)
            # Also handle images links: <a href="[^"]*">...<img ...alt="Project">...</a>
            # This is harder, but usually the title link is enough if both are updated
            # Let's try to find the block
            
    # Special fix for image links in portfolios.html
    if 'portfolios.html' in filepath:
        # Manual fix for the 4 items
        content = content.replace('href="tech-integration.html">Business Analytics & Reporting', 'href="tech-integration.html">Business Analytics & Reporting') # Already correct
        content = content.replace('href="tech-integration.html">Sales and Marketing Strategy', 'href="market-expansion.html">Sales and Marketing Strategy')
        content = content.replace('href="tech-integration.html">Business Process Optimization', 'href="operational-excellence.html">Business Process Optimization')

    # 4. Circular Navigation Cleanup
    # Ensure only ONE navigation block exists
    nav_pattern = re.compile(r'<!-- navigation -->.*?</div>\s*</div>', re.DOTALL)
    # Actually, the pattern is usually:
    # <!-- navigation -->
    # <div class="pxn_post_navigation">...</div>
    
    # Let's find the circular logic for this specific page
    filename = os.path.basename(filepath)
    
    prev_link = "#"
    next_link = "#"
    
    # Portfolio Circular
    if filename in portfolio_pages:
        idx = portfolio_pages.index(filename)
        prev_link = portfolio_pages[(idx - 1) % len(portfolio_pages)]
        next_link = portfolio_pages[(idx + 1) % len(portfolio_pages)]
    # Service Circular
    elif filename in [s[0] for s in services]:
        s_list = [s[0] for s in services]
        idx = s_list.index(filename)
        prev_link = s_list[(idx - 1) % len(s_list)]
        next_link = s_list[(idx + 1) % len(s_list)]
    # Blog Circular
    elif filename in blog_pages:
        idx = blog_pages.index(filename)
        prev_link = blog_pages[(idx - 1) % len(blog_pages)]
        next_link = blog_pages[(idx + 1) % len(blog_pages)]

    if prev_link != "#" or next_link != "#":
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
        
        # Replace existing navigation block if it exists
        if '<div class="pxn_post_navigation">' in content:
            content = re.sub(r'(<!-- navigation -->\s*)?<div class="pxn_post_navigation">.*?</div>', new_nav, content, flags=re.DOTALL)
        else:
            # Inject before Sidebar or at end of content?
            # Usually it's after the content
            content = content.replace('<!-- end: Post Content -->', '<!-- end: Post Content -->\n                  ' + new_nav)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to all relevant files
all_files = [s[0] for s in services] + portfolio_pages + blog_pages + ['index.html', 'portfolios.html', 'about.html', 'contact.html']
for f in all_files:
    if os.path.exists(f):
        fix_file(f)
        print(f"Fixed {f}")

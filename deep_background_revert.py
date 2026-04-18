import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Detailed Reversion Map based on previous aggressive scrubbing
detailed_reversion = {
    # Hero Slider (index.html)
    r'data-bg-image="https://images\.unsplash\.com/photo-1557804506-669a67965ba0\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/hero/h1-hero-slider-img-2.jpg"',
    
    # Why Choose (index.html and others)
    r'data-bg-image="https://images\.unsplash\.com/photo-1551434678-e076c223a692\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/why-choose/h1-why-choose-bg-img.png"',
    
    # Page Header (About, Services, etc.)
    r'data-bg-image="https://images\.unsplash\.com/photo-1497366216548-37526070297c\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/page-header/page-header-bg.jpg"',
    
    # Footer (Double check site-wide)
    r'data-bg-image="https://images\.unsplash\.com/photo-1451187580459-43490279c0fa\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/footer/h1-footer-bg.png"',
}

# Generic cleanup for any other data-bg-image that points to Unsplash
# but keep specific ones above if they differ.
generic_bg_reversion = r'data-bg-image="https://images\.unsplash\.com/photo-[^"]*"'

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply specific reversions
    for pattern, replacement in detailed_reversion.items():
        content = re.sub(pattern, replacement, content)
    
    # Also catch some 'src' backgrounds if they were used as backgrounds
    # (Though usually it's data-bg-image)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Specified background images reverted to original template paths site-wide.")

import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# The Ultimate Reversion Map
reversions = {
    # Background Images (data-bg-image)
    r'data-bg-image="https://images\.unsplash\.com/photo-1497366216548-37526070297c\?auto=format&fit=crop&w=1200&q=80"': 'data-bg-image="./assets/images/progress/h3-progress-bg-img.jpg"',
    r'data-bg-image="https://images\.unsplash\.com/photo-1522202176988-66273c2fd55f\?auto=format&fit=crop&w=800&q=80"': 'data-bg-image="./assets/images/projects/sidebar-cta-bg.jpg"',
    
    # Regular Images (src) that I might have touched
    r'src="https://images\.unsplash\.com/photo-1522202176988-66273c2fd55f\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/about/h1-about-img-1.jpg"',
    r'src="https://images\.unsplash\.com/photo-1522202176988-66273c2fd55f\?auto=format&fit=crop&w=400&h=400&q=80"': 'src="./assets/images/about/h1-about-img-2.jpg"',
}

# Add the ones from the previous script just in case
reversions.update({
    r'data-bg-image="https://images\.unsplash\.com/photo-1557804506-669a67965ba0\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/hero/h1-hero-slider-img-2.jpg"',
    r'data-bg-image="https://images\.unsplash\.com/photo-1551434678-e076c223a692\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/why-choose/h1-why-choose-bg-img.png"',
    r'data-bg-image="https://images\.unsplash\.com/photo-1497366216548-37526070297c\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/page-header/page-header-bg.jpg"',
    r'data-bg-image="https://images\.unsplash\.com/photo-1451187580459-43490279c0fa\?auto=format&fit=crop&w=1920&q=80"': 'data-bg-image="./assets/images/footer/h1-footer-bg.png"',
})

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in reversions.items():
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Comprehensive background and primary image reversion complete.")

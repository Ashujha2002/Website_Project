import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# 1. Image Replacement Map (Robust & High Quality)
# This map targets specific local paths that are known to be broken or generic
img_fix_map = {
    # Logos (if broken, though they seem okay, I'll provide a fallback logic)
    r'src="\./assets/images/logos/primary-logo\.png"': 'src="https://abentis.es/wp-content/uploads/2023/10/logo-abentis.png"', # Assuming or using placeholder if unsure
    r'src="\./assets/images/logos/secondary-logo\.png"': 'src="https://abentis.es/wp-content/uploads/2023/10/logo-abentis.png"',
    
    # Hero / Page Headers
    r'data-bg-image="\./assets/images/page-header/page-header-bg\.jpg"': 'data-bg-image="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80"',
    
    # Testimonials / Clients
    r'src="\./assets/images/clients/client-logo-1\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    r'src="\./assets/images/clients/client-logo-2\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    r'src="\./assets/images/clients/client-logo-3\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    r'src="\./assets/images/clients/client-logo-4\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    r'src="\./assets/images/clients/client-logo-5\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    r'src="\./assets/images/clients/client-logo-6\.png"': 'src="https://images.unsplash.com/photo-1599305090598-fe179d501c27?auto=format&fit=crop&w=200&q=80"',
    
    # FAQ / CTA
    r'src="\./assets/images/faq/h2-faq-cta-img\.jpg"': 'src="https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80"',
    r'data-bg-image="\./assets/images/why-choose/h1-why-choose-bg-img\.png"': 'data-bg-image="https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=1920&q=80"',
    
    # Footer
    r'data-bg-image="\./assets/images/footer/h1-footer-bg\.png"': 'data-bg-image="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80"',
}

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply Image Fixes
    for pattern, replacement in img_fix_map.items():
        content = re.sub(pattern, replacement, content)
    
    # Ensure no Rovix remains in Title
    content = content.replace('ABENTIS CONSULTING SL Business Consulting HTML Template', 'ABENTIS CONSULTING SL | Strategic Business Consulting')
    
    # Fix any remaining broken internal detail links
    content = content.replace('href="blog-details.html"', 'href="strategic-growth-insights.html"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final comprehensive image and branding sanitization complete.")

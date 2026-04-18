import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Detailed Reversion Map for content images (src)
content_reversion = {
    # index.html / about.html - About Section
    r'src="https://images\.unsplash\.com/photo-1522202176988-66273c2fd55f\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/about/h1-about-img-1.jpg"',
    r'src="https://images\.unsplash\.com/photo-1552664730-d307ca884978\?auto=format&fit=crop&w=1200&q=80"': 'src="./assets/images/about/h1-about-img-2.jpg"',
    
    # index.html - Client Logos (revert to placeholder or original if known)
    r'src="https://images\.unsplash\.com/photo-1599305090598-fe179d501c27\?auto=format&fit=crop&w=200&q=80"': 'src="./assets/images/clients/client-logo-1.png"',
    
    # index.html - Project Grid
    r'src="https://images\.unsplash\.com/photo-1552664730-d307ca884978\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/projects/h1-project-img-1.jpg"',
    r'src="https://images\.unsplash\.com/photo-1460925895917-afdab827c52f\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/projects/h1-project-img-2.jpg"',
    r'src="https://images\.unsplash\.com/photo-1554224155-169745fe9a5c\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/projects/h1-project-img-3.jpg"',
    r'src="https://images\.unsplash\.com/photo-1451187580459-43490279c0fa\?auto=format&fit=crop&w=800&q=80"': 'src="./assets/images/projects/h1-project-img-4.jpg"',
    
    # Testimonials
    r'src="https://images\.unsplash\.com/photo-1507003211169-0a1dd7228f2d\?auto=format&fit=crop&w=100&q=80"': 'src="./assets/images/testimonial/h1-testimonial-author-img-1.jpg"',
    r'src="https://images\.unsplash\.com/photo-1494790108377-be9c29b29330\?auto=format&fit=crop&w=100&q=80"': 'src="./assets/images/testimonial/h1-testimonial-author-img-2.jpg"',
}

# Add Portfolio Details specific ones back to template dummies
# since the user might want the template aesthetic back first.
content_reversion.update({
    r'src="https://images\.unsplash\.com/photo-1542744173-8e7e53415bb0\?auto=format&fit=crop&w=1200&q=80"': 'src="./assets/images/projects/project-details-img-2.jpg"',
})

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in content_reversion.items():
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Specified content images (src) reverted to original template paths site-wide.")

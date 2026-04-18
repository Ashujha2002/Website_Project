import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Reversion Map: Remote Unsplash -> Original Local Path
reversion_map = {
    # Page Header
    'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80': './assets/images/page-header/page-header-bg.jpg',
    
    # Why Choose Us BG
    'https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=1920&q=80': './assets/images/why-choose/h1-why-choose-bg-img.png',
    
    # Any other common ones I might have injected
    'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80': './assets/images/services/h2-service-bg-img.jpg',
}

# Also revert logos if I changed them
logo_reversion = {
    'https://abentis.es/wp-content/uploads/2023/10/logo-abentis.png': './assets/images/logos/primary-logo.png'
}

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Revert Backgrounds
    for remote, local in reversion_map.items():
        # Match data-bg-image="remote"
        content = content.replace(f'data-bg-image="{remote}"', f'data-bg-image="{local}"')
        # Also match plain URLs in case they were injected differently
        content = content.replace(remote, local)
        
    # Revert Logos
    for remote, local in logo_reversion.items():
        content = content.replace(f'src="{remote}"', f'src="{local}"')
        content = content.replace(remote, local)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Background images and logos reverted to original template paths site-wide.")

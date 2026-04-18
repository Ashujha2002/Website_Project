import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'

# Portfolio Pages in order
portfolios = [
    'operational-excellence.html',
    'market-expansion.html',
    'financial-restructuring.html',
    'tech-integration.html'
]

# Blog Pages in order
blogs = [
    'strategic-growth-insights.html',
    'digital-transformation-trends.html',
    'efficient-operations-guide.html'
]

def update_navigation(pages):
    for i, page in enumerate(pages):
        filepath = os.path.join(directory, page)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        prev_page = pages[(i - 1) % len(pages)]
        next_page = pages[(i + 1) % len(pages)]
        
        # Update Previous Link
        # Match <a href="..." class="navigation prev">
        content = re.sub(r'(<a\s+href=")[^"]*("\s+class="navigation\s+prev">)', f'\\1{prev_page}\\2', content)
        content = re.sub(r'(<a\s+class="navigation\s+prev"\s+href=")[^"]*(">)', f'\\1{prev_page}\\2', content)
        
        # Update Next Link
        # Match <a href="..." class="navigation next">
        content = re.sub(r'(<a\s+href=")[^"]*("\s+class="navigation\s+next">)', f'\\1{next_page}\\2', content)
        content = re.sub(r'(<a\s+class="navigation\s+next"\s+href=")[^"]*(">)', f'\\1{next_page}\\2', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# Update Portfolio and Blog navigations
update_navigation(portfolios)
update_navigation(blogs)

print("Portfolio and Blog navigation links have been updated to a circular flow.")

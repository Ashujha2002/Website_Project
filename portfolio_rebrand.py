import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
template_path = os.path.join(directory, 'portfolio-details.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

portfolio_data = {
    "operational-excellence.html": {
        "title": "Operational Excellence",
        "h2": "Powering efficient operations with modern solutions.",
        "p1": "We partnered with a leading manufacturing firm to streamline their core production workflows. By implementing Lean methodologies and real-time monitoring systems, we achieved a 30% reduction in operational waste and significantly improved time-to-market for new product lines.",
        "p2": "The project involved a deep dive into resource allocation, supply chain logistics, and employee productivity. Our final roadmap provided a scalable framework for continuous improvement and sustainable operational health.",
        "overview": "Our consulting team focused on identifying bottlenecks and implementing high-impact efficiency tools across the organization.",
        "features": ["Workflow Optimization", "Lean Manufacturing Implementation", "Resource Efficiency Planning", "Performance Tracking Systems"],
        "client": "Ethan Roberts",
        "category": "Operational Strategy",
        "service": "Corporate Consulting",
        "date": "15 Jan 2026",
        "main_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1200",
        "second_img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&q=80&w=800"
    },
    "market-expansion.html": {
        "title": "Market Expansion",
        "h2": "Scaling business horizons in emerging markets.",
        "p1": "For a growing retail brand, we developed a comprehensive market entry strategy for the European region. Our data-driven approach identified high-potential territories and defined the localized marketing and distribution channels required for a successful launch.",
        "p2": "We provided end-to-end support, from regulatory compliance analysis to competitor benchmarking. The brand successfully captured a 15% market share within the first 12 months of operation.",
        "overview": "This project showcases our ability to translate complex market data into actionable growth strategies for international expansion.",
        "features": ["Territory Analysis", "Localized Marketing Strategy", "Regulatory Compliance Support", "Competitor Benchmarking"],
        "client": "Sophia Martinez",
        "category": "Growth Strategy",
        "service": "International Expansion",
        "date": "22 Jan 2026",
        "main_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1200",
        "second_img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800"
    },
    "financial-restructuring.html": {
        "title": "Financial Restructuring",
        "h2": "Stabilizing corporate health through strategic finance.",
        "p1": "We assisted a mid-sized logistics company in navigating a complex financial restructuring phase. By optimizing their capital structure and renegotiating debt obligations, we provided the liquidity needed to fund their next phase of innovation.",
        "p2": "Our financial experts implemented rigorous forecasting models and cost-control measures that restored investor confidence and secured a stable financial future for the organization.",
        "overview": "A critical project that demonstrated our expertise in high-stakes financial management and corporate stabilization.",
        "features": ["Capital Structure Optimization", "Debt Renegotiation Support", "Cash Flow Forecasting", "Cost-Control Implementation"],
        "client": "Liam O'Connor",
        "category": "Finance",
        "service": "Corporate Restructuring",
        "date": "05 Feb 2026",
        "main_img": "https://images.unsplash.com/photo-1554224155-169745fe9a5c?auto=format&fit=crop&q=80&w=1200",
        "second_img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&q=80&w=800"
    },
    "tech-integration.html": {
        "title": "Tech Integration",
        "h2": "Modernizing legacy systems for digital-first growth.",
        "p1": "We led the digital transformation of a legacy insurance firm, migrating their core operations to a cloud-native architecture. This integration enabled seamless data flow across departments and enhanced their customer service capabilities through automated workflows.",
        "p2": "The project resulted in a significant reduction in IT maintenance costs and provided a robust platform for future technological innovations and AI-driven insights.",
        "overview": "Our team provided the technical roadmap and implementation support for a complete digital overhaul.",
        "features": ["Cloud Migration Strategy", "Legacy System Modernization", "Automated Workflow Design", "Data Integration Framework"],
        "client": "Olivia Chen",
        "category": "Technology",
        "service": "Digital Transformation",
        "date": "18 Feb 2026",
        "main_img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1200",
        "second_img": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=800"
    }
}

def generate_portfolio_page(filename, data):
    content = template_html
    # Titles
    content = content.replace("<title>ABENTIS CONSULTING SL Business Consulting HTML Template</title>", f"<title>{data['title']} - ABENTIS CONSULTING SL</title>")
    content = content.replace('<h1 class="page_title">Portfolio Details</h1>', f'<h1 class="page_title">{data["title"]}</h1>')
    content = content.replace('<span class="current">Portfolio Details</span>', f'<span class="current">{data["title"]}</span>')
    
    # Main Content
    content = re.sub(r'<h2>Powering efficient operations with modern solutions\.</h2>', f'<h2>{data["h2"]}</h2>', content)
    # Paragraphs replacement
    p_pattern = r'<p>Our portfolio reflects a proven track record.*?goals\.</p>\s*<p>Explore our portfolio to see how we transform.*?real business challenges turned \.\.</p>'
    new_ps = f'<p>{data["p1"]}</p>\n<p>{data["p2"]}</p>'
    content = re.sub(p_pattern, new_ps, content, flags=re.DOTALL)
    
    # Overview and Features
    content = re.sub(r'<p>Our consulting portfolio showcases successful partner-.*?industries\.</p>', f'<p>{data["overview"]}</p>', content, flags=re.DOTALL)
    features_html = "".join([f'<li><i class="pxni-checked"></i> {f}</li>' for f in data["features"]])
    content = re.sub(r'<ul class="pxn_list">.*?</ul>', f'<ul class="pxn_list">{features_html}</ul>', content, flags=re.DOTALL)
    
    # Images
    content = content.replace('./assets/images/projects/project-details-img-1.jpg', data["main_img"])
    # There was an empty col for the second image area in template, let's put it back if missing
    content = content.replace('<div class="col-12 col-md-6 col-lg-12 col-xl-6">\n                      \n                    </div>', f'<div class="col-12 col-md-6 col-lg-12 col-xl-6"><img src="{data["second_img"]}" alt="Image"></div>')

    # Sidebar Info
    content = re.sub(r'<li>\s*<span class="label">Clients</span>\s*<span class="value">.*?</span>\s*</li>', f'<li><span class="label">Clients</span><span class="value">{data["client"]}</span></li>', content, flags=re.DOTALL)
    content = re.sub(r'<li>\s*<span class="label">Portfolio</span>\s*<span class="value">.*?</span>\s*</li>', f'<li><span class="label">Portfolio</span><span class="value">{data["title"]}</span></li>', content, flags=re.DOTALL)
    content = re.sub(r'<li>\s*<span class="label">Service</span>\s*<span class="value">.*?</span>\s*</li>', f'<li><span class="label">Service</span><span class="value">{data["service"]}</span></li>', content, flags=re.DOTALL)
    content = re.sub(r'<li>\s*<span class="label">Category</span>\s*<span class="value">.*?</span>\s*</li>', f'<li><span class="label">Category</span><span class="value">{data["category"]}</span></li>', content, flags=re.DOTALL)
    content = re.sub(r'<li>\s*<span class="label">Date</span>\s*<span class="value">.*?</span>\s*</li>', f'<li><span class="label">Date</span><span class="value">{data["date"]}</span></li>', content, flags=re.DOTALL)

    return content

# Generate the files
for filename, data in portfolio_data.items():
    page_html = generate_portfolio_page(filename, data)
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(page_html)

# Now Update Navigation site-wide
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Drodown links for Portfolios
dropdown_links = ""
for f, d in portfolio_data.items():
    dropdown_links += f'<li><a href="{f}">{d["title"]}</a></li>'

# Nav replacement pattern for Portfolios dropdown
# Target:
# <li class="has-dropdown[^"]*"><a href="#">Portfolios</a>
#   <ul class="sub-menu">
#     ...
#   </ul>
# </li>
nav_pattern = r'<li class="has-dropdown[^"]*"><a href="[^"]*">Portfolios</a>\s*<ul class="sub-menu">.*?</ul>\s*</li>'
new_nav = f'<li class="has-dropdown"><a href="#">Portfolios</a><ul class="sub-menu">{dropdown_links}</ul></li>'

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace dropdown
    c = re.sub(nav_pattern, new_nav, c, flags=re.DOTALL)
    
    # Final cleanup (ensure no video etc)
    c = c.replace('<i class="pxni-phone"></i>', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

print("4 Unique Portfolio pages created and Navigation updated site-wide.")

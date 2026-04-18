import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
template_file = os.path.join(directory, 'service-details.html')

with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Define Service Details
services = {
    "business-process.html": {
        "title": "Business Process",
        "desc": "Analyze and improve your internal business processes. We focus on enhancing operational flow and ensuring every step in your value chain is optimized for efficiency.",
        "features": ["Process Mapping", "Value Chain Analysis", "Bottleneck Identification", "Operational Flow"],
        "docs": ["Process Map", "Efficiency Report", "Operational Audit", "Improvement Plan"]
    },
    "financial-management.html": {
        "title": "Financial Management",
        "desc": "Optimize your financial health with expert planning. We provide guidance on budgeting, cash flow management, and investment strategies to ensure long-term stability.",
        "features": ["Budget Planning", "Cash Flow Analysis", "Investment Strategy", "Financial Reporting"],
        "docs": ["Financial Audit", "Budget Forecast", "Cash Flow Projection", "Reporting Framework"]
    },
    "market-research.html": {
        "title": "Market Research",
        "desc": "Gain deep insights into your industry and audience. Our research helps you understand customer needs, market gaps, and emerging trends to stay ahead of the competition.",
        "features": ["Customer Insights", "Market Gap Analysis", "Trend Forecasting", "Survey Design"],
        "docs": ["Research Report", "Customer Persona", "Trend Analysis", "Competitive Landscape"]
    },
    "change-management.html": {
        "title": "Change Management",
        "desc": "Navigating organizational change is complex. We provide the tools and strategies to ensure your team transitions smoothly during mergers, restructuring, or cultural shifts.",
        "features": ["Transition Planning", "Stakeholder Communication", "Cultural Alignment", "Training Programs"],
        "docs": ["Change Management Strategy", "Communication Plan", "Training Curriculum", "Readiness Assessment"]
    },
    "strategic-planning.html": { "title": "Strategic Planning", "desc": "Defined vision and actionable goals.", "features": ["Trend Analysis"], "docs": ["Roadmap"] },
    "digital-transformation.html": { "title": "Digital Transformation", "desc": "Modernize your business.", "features": ["Digital Strategy"], "docs": ["Audit"] },
    "risk-management.html": { "title": "Risk Management", "desc": "Identify and mitigate risks.", "features": ["Compliance"], "docs": ["Risk Register"] }
}

# Function to generate unique page content
def generate_page(filename, data):
    content = template_content
    # Update Page Title and Metadata
    content = content.replace('<title>ABENTIS CONSULTING SL Business Consulting HTML Template</title>', f'<title>{data["title"]} - ABENTIS CONSULTING SL</title>')
    content = content.replace('<h1 class="page_title">Service Details</h1>', f'<h1 class="page_title">{data["title"]}</h1>')
    content = content.replace('<span class="current">Service Details</span>', f'<span class="current">{data["title"]}</span>')
    
    # Update Main Heading and Description
    content = content.replace('<h2>Explore our Service Lists</h2>', f'<h2>{data["title"]} Services</h2>')
    desc_pattern = r'<p>Our business consulting services are designed to help organizations navigate complexity.*?</p>'
    content = re.sub(desc_pattern, f'<p>{data["desc"]}</p>', content, flags=re.DOTALL)
    
    # Update Mistake section
    content = content.replace('<h3>Mistakes to avoid to the dummy</h3>', f'<h3>Why {data["title"]} Matters</h3>')
    
    # Update Features List
    features_html = "".join([f'<li><i class="pxni-checked"></i> {f}</li>' for f in data["features"]])
    content = re.sub(r'<ul class="pxn_list">.*?</ul>', f'<ul class="pxn_list">{features_html}</ul>', content, count=1, flags=re.DOTALL)
    
    # Update Document Required
    docs_html = ""
    for doc in data["docs"]:
        docs_html += f'''
                    <div class="pxn_icon_box_2">
                      <div class="box_icon"><i class="pxni-checked-circle-2"></i></div>
                      <div class="box_content">
                        <h3 class="box_title">{doc}</h3>
                        <div class="box_desc">Professional support for {doc.lower()} implementation.</div>
                      </div>
                    </div>'''
    content = re.sub(r'<div class="icon_box_wrap mb-30">.*?</div>\s*</div>', f'<div class="icon_box_wrap mb-30">{docs_html}</div>\n                  </div>', content, count=1, flags=re.DOTALL)

    # Sidebar
    sidebar_links = ""
    for s_file, s_data in services.items():
        active_class = "active" if s_file == filename else ""
        sidebar_links += f'<li><a class="service {active_class}" href="{s_file}"><span class="service_title">{s_data["title"]}</span><span class="service_icon"><span><i class="pxni-arrow-right"></i><i class="pxni-arrow-right"></i></span></span></a></li>'
    content = re.sub(r'<ul class="pxn_services_list">.*?</ul>', f'<ul class="pxn_services_list">{sidebar_links}</ul>', content, flags=re.DOTALL)

    return content

# Create/Update service pages
for filename, data in services.items():
    page_content = generate_page(filename, data)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_content)

# Footer sections from screenshot
our_services_footer = '''
                        <li><a href="business-process.html">Business Process</a></li>
                        <li><a href="financial-management.html">Financial Management</a></li>
                        <li><a href="market-research.html">Market Research</a></li>
                        <li><a href="change-management.html">Change Management</a></li>
                        <li><a href="market-research.html">Market Research</a></li>'''

resources_footer = '''
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="portfolios.html">Our Portfolio</a></li>
                        <li><a href="blog.html">Blog Post</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="pricing.html">Pricing Page</a></li>'''

all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Footer Services
    content = re.sub(r'<h2 class="footer_title">Our Services</h2>\s*<ul>.*?</ul>', f'<h2 class="footer_title">Our Services</h2>\n                      <ul>{our_services_footer}</ul>', content, flags=re.DOTALL)
    # Footer Resources
    content = re.sub(r'<h2 class="footer_title">Resources</h2>\s*<ul>.*?</ul>', f'<h2 class="footer_title">Resources</h2>\n                      <ul>{resources_footer}</ul>', content, flags=re.DOTALL)

    # Global Cleanup
    content = content.replace('Seattle (major city in the state Washington).', 'Calle de la Paz, 1, 28012 Madrid')
    content = content.replace('Shanghai (major global financial hub & China\'s largest cities)', 'Av. Diagonal, 405, 08008 Barcelona')
    content = content.replace('Refresh your skills, our team of experienced instructors will guide you every step the way. Our comprehensive...', 'Empowering businesses with strategic insights and operational excellence.')
    content = content.replace('Mistakes to avoid to the dummy', 'Professional Insights & Strategies')
    content = content.replace('Rovix', 'ABENTIS CONSULTING SL')
    content = content.replace('dummy text', 'professional content')
    content = content.replace('Lorem Ipsum', 'Abentis Consulting')

    # Fix CIF
    content = content.replace('+880 (123) 456 789', 'B95533089')
    content = content.replace('+880123456789', 'B95533089')
    content = re.sub(r'href="tel:\+880\d+"', 'href="contact.html"', content)

    # Remove social
    content = re.sub(r'<ul class="[^"]*social[^"]*">.*?</ul>', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer and pages updated as per screenshot.")

import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
template_file = os.path.join(directory, 'service-details.html')

with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Define Service Details
services = {
    "strategic-planning.html": {
        "title": "Strategic Planning",
        "desc": "Our strategic planning services help organizations define their long-term vision and set actionable goals. We analyze market trends and internal capabilities to create a roadmap for sustainable success.",
        "features": ["Market Trend Analysis", "Long-term Goal Setting", "Resource Allocation", "Vision & Mission Definition"],
        "docs": ["Strategic Vision Document", "Market Analysis Report", "Actionable Roadmap", "KPI Framework"],
        "main_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"
    },
    "digital-transformation.html": {
        "title": "Digital Transformation",
        "desc": "Modernize your business workflows and customer experience through innovative digital strategies. We provide the technology roadmap for your future growth.",
        "features": ["Cloud Solutions", "Legacy System Migration", "Digital Customer Experience", "Data Analytics"],
        "docs": ["Digital Audit Report", "Technology Stack Plan", "Transformation Roadmap", "Security Assessment"],
        "main_img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80"
    },
    "risk-management.html": {
        "title": "Risk Management",
        "desc": "Identify and mitigate potential risks while ensuring complete regulatory compliance. Protect your business assets and reputation with our proven frameworks.",
        "features": ["Compliance Auditing", "Risk Assessment", "Business Continuity", "Fraud Prevention"],
        "docs": ["Risk Management Plan", "Compliance Registry", "Mitigation Strategy", "Audit Findings"],
        "main_img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&w=800&q=80"
    },
    "business-process.html": {
        "title": "Business Process",
        "desc": "Streamline your operations and enhance value creation through process optimization. We help you eliminate waste and focus on what truly matters for your customers.",
        "features": ["Process Mapping", "Operational Efficiency", "Supply Chain Optimization", "Quality Control"],
        "docs": ["Process Audit", "Workflow Optimization Plan", "Supply Chain Strategy", "Efficiency Report"],
        "main_img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&w=800&q=80"
    },
    "financial-management.html": {
        "title": "Financial Management",
        "desc": "Optimize your capital allocation and financial health. Our experts provide precise forecasting and budgeting tools to ensure long-term stability and growth.",
        "features": ["Cash Flow Management", "Investment Advisory", "Budget Forecasting", "Financial Auditing"],
        "docs": ["Budget Plan", "Investment Portfolio", "Financial Health Report", "Cash Flow Projection"],
        "main_img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1554224155-169745fe9a5c?auto=format&fit=crop&w=800&q=80"
    },
    "market-research.html": {
        "title": "Market Research",
        "desc": "Understand your market dynamics and competitor landscape with data-driven insights. We help you identify growth opportunities and customer needs.",
        "features": ["Consumer Behavior Analysis", "Competitive Intelligence", "Market Sizing", "Trend Forecasting"],
        "docs": ["Market Insight Report", "Competitor Profile", "Customer Persona", "Survey Analysis"],
        "main_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1551288049-bbbda536339a?auto=format&fit=crop&w=800&q=80"
    },
    "business-optimization.html": {
        "title": "Business Optimization",
        "desc": "Drive operational excellence across all levels of your organization. We identify performance gaps and implement strategies for superior business results.",
        "features": ["Performance Benchmarking", "Productivity Enhancement", "Profitability Analysis", "Asset Management"],
        "docs": ["Optimization Plan", "Performance Metrics", "Asset Audit", "Profitability Report"],
        "main_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&w=800&q=80"
    },
    "it-consulting.html": {
        "title": "IT Consulting",
        "desc": "Modernize your IT infrastructure and align it with your business strategy. We provide expert guidance on software selection, security, and digital architecture.",
        "features": ["IT Strategy", "Infrastructure Design", "Software Architecture", "Tech Security"],
        "docs": ["IT Roadmap", "Infrastructure Audit", "Tech Stack Assessment", "Security Policy"],
        "main_img": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80"
    },
    "change-management.html": {
        "title": "Change Management",
        "desc": "Navigate organizational transitions smoothly with our expert change management strategies. We focus on cultural alignment and stakeholder communication.",
        "features": ["Organizational Readiness", "Communication Strategy", "Leadership Alignment", "Culture Shift"],
        "docs": ["Change Readiness Report", "Stakeholder Communication", "Training Plan", "Cultural Integration"],
        "main_img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&w=800&q=80"
    },
    "leadership.html": {
        "title": "Leadership",
        "desc": "Develop the leadership skills necessary to drive organizational success. We provide executive coaching and strategic vision development for modern leaders.",
        "features": ["Executive Coaching", "Team Building", "Strategic Vision", "Decision Making"],
        "docs": ["Leadership Assessment", "Development Roadmap", "Executive Coaching Plan", "Performance Review"],
        "main_img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=800&q=80"
    },
    "growth-expansion.html": {
        "title": "Growth & Expansion",
        "desc": "Expand your business into new territories and markets with confidence. We provide the market analysis and scaling strategies for sustainable expansion.",
        "features": ["Market Entry Strategy", "Scalability Planning", "Growth Modeling", "Feasibility Analysis"],
        "docs": ["Growth Strategy", "Expansion Feasibility", "Market Entry Roadmap", "Scalability Audit"],
        "main_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "second_img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80"
    }
}

# Generate Service Pages
def generate_service_page(filename, data):
    content = template_content
    content = content.replace('<title>ABENTIS CONSULTING SL Business Consulting HTML Template</title>', f'<title>{data["title"]} - ABENTIS CONSULTING SL</title>')
    content = content.replace('<h1 class="page_title">Service Details</h1>', f'<h1 class="page_title">{data["title"]}</h1>')
    content = content.replace('<span class="current">Service Details</span>', f'<span class="current">{data["title"]}</span>')
    content = content.replace('<h2>Explore our Service Lists</h2>', f'<h2>{data["title"]} Solutions</h2>')
    desc_pattern = r'<p>Our business consulting services are designed to help organizations navigate complexity.*?</p>'
    content = re.sub(desc_pattern, f'<p>{data["desc"]}</p>', content, flags=re.DOTALL)
    content = content.replace('./assets/images/services/service-details-img-1.jpg', data["main_img"])
    content = content.replace('./assets/images/services/service-details-img-2.jpg', data["second_img"])
    features_html = "".join([f'<li><i class="pxni-checked"></i> {f}</li>' for f in data["features"]])
    content = re.sub(r'<ul class="pxn_list">.*?</ul>', f'<ul class="pxn_list">{features_html}</ul>', content, count=1, flags=re.DOTALL)
    docs_html = ""
    for doc in data["docs"]:
        docs_html += f'''
                    <div class="pxn_icon_box_2">
                      <div class="box_icon"><i class="pxni-checked-circle-2"></i></div>
                      <div class="box_content">
                        <h3 class="box_title">{doc}</h3>
                        <div class="box_desc">Professional support for {doc.lower()} implementation and tracking.</div>
                      </div>
                    </div>'''
    content = re.sub(r'<div class="icon_box_wrap mb-30">.*?</div>\s*</div>', f'<div class="icon_box_wrap mb-30">{docs_html}</div>\n                  </div>', content, count=1, flags=re.DOTALL)
    return content

for filename, data in services.items():
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(generate_service_page(filename, data))

# Global Updates
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Pricing Plan Section
    content = re.sub(r'<!-- start: Pricing Section -->.*?<!-- end: Pricing Section -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<section class="[^"]*pricing[^"]*">.*?</section>', '', content, flags=re.DOTALL)
    # Remove Pricing Page from menus
    content = re.sub(r'<li><a href="pricing.html">Pricing Page</a></li>', '', content)

    # 2. Remove all "Read More" text
    content = content.replace('Read More', '')
    content = content.replace('Read more', '')
    content = content.replace('More Details', 'Explore') # Replace other similar text if needed, user said "Read More text"

    # 3. Remove all external links (point to #)
    external_links = re.findall(r'href="(https?://[^"]+)"', content)
    for link in external_links:
        if "unsplash.com" not in link and "youtube.com" not in link and "google.com" not in link:
            content = content.replace(link, '#')

    # 4. Fix Contact Page CIF icon
    if filename == 'contact.html':
        content = content.replace('pxni-phone', 'pxni-shield-check')

    # 5. Fix Homepage Service Links
    if filename == 'index.html':
        content = content.replace('<h3 class="offer_title">Growth & Expansion <br>Consulting</h3>', '<h3 class="offer_title"><a href="growth-expansion.html">Growth & Expansion <br>Consulting</a></h3>')
        content = content.replace('<h3 class="offer_title">Digital Transformation <br>Consulting</h3>', '<h3 class="offer_title"><a href="digital-transformation.html">Digital Transformation <br>Consulting</a></h3>')
        content = content.replace('<h3 class="offer_title">Risk Management <br>& Compliance</h3>', '<h3 class="offer_title"><a href="risk-management.html">Risk Management <br>& Compliance</a></h3>')
        # Also images on index
        content = content.replace('./assets/images/about/h1-about-img-1.jpg', 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80')
        content = content.replace('./assets/images/about/h1-about-img-2.jpg', 'https://images.unsplash.com/photo-1517245327032-9792f6895c02?auto=format&fit=crop&w=400&h=400&q=80')

    # 6. Correct Dropdown Menu for Services (11 services)
    dropdown_html = '''
                        <li class="has-dropdown"><a href="#">Services</a>
                          <ul class="sub-menu">
                            <li><a href="services.html">All Services</a></li>
                            <li><a href="strategic-planning.html">Strategic Planning</a></li>
                            <li><a href="digital-transformation.html">Digital Transformation</a></li>
                            <li><a href="risk-management.html">Risk Management</a></li>
                            <li><a href="business-process.html">Business Process</a></li>
                            <li><a href="financial-management.html">Financial Management</a></li>
                            <li><a href="market-research.html">Market Research</a></li>
                            <li><a href="business-optimization.html">Business Optimization</a></li>
                            <li><a href="it-consulting.html">IT Consulting</a></li>
                            <li><a href="change-management.html">Change Management</a></li>
                            <li><a href="leadership.html">Leadership</a></li>
                            <li><a href="growth-expansion.html">Growth & Expansion</a></li>
                          </ul>
                        </li>'''
    content = re.sub(r'<li class="has-dropdown[^"]*"><a href="#">Services</a>\s*<ul class="sub-menu">.*?</ul>\s*</li>', dropdown_html, content, flags=re.DOTALL)

    # 7. Update Footer (Remove Pricing)
    footer_res_html = '''
                      <h2 class="footer_title">Resources</h2>
                      <ul>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="portfolios.html">Our Portfolio</a></li>
                        <li><a href="blog.html">Blog Post</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                      </ul>'''
    content = re.sub(r'<h2 class="footer_title">Resources</h2>\s*<ul>.*?</ul>', footer_res_html, content, flags=re.DOTALL)

    # Global Image fix
    content = content.replace('./assets/images/hero/h1-hero-slider-1.jpg', 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80')
    content = content.replace('./assets/images/hero/h1-hero-slider-2.jpg', 'https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=1920&q=80')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Delete pricing.html
pricing_file = os.path.join(directory, 'pricing.html')
if os.path.exists(pricing_file):
    os.remove(pricing_file)

print("Master cleanup and service page generation complete.")

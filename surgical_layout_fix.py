import os

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
template_path = os.path.join(directory, 'service-details.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# 1. Prepare the template by removing the video section
# In service-details.html, the video section is:
# <div class="pxn_video mt-30 mb-30"> ... </div>
import re
template_content = re.sub(r'<div class="pxn_video[^"]*">.*?</div>', '', template_content, flags=re.DOTALL)
template_content = re.sub(r'<a[^>]*class="[^"]*video_popup[^"]*"[^>]*>.*?</a>', '', template_content, flags=re.DOTALL)

services_data = {
    "strategic-planning.html": {
        "title": "Strategic Planning",
        "desc": "Our strategic planning services help organizations define their long-term vision and set actionable goals. We analyze market trends and internal capabilities to create a roadmap for sustainable success.",
        "features": ["Market Trend Analysis", "Long-term Goal Setting", "Resource Allocation", "Vision & Mission Definition"],
        "docs": [
            ("Strategic Vision", "Detailed roadmap for long-term growth and market leadership."),
            ("Market Analysis", "Comprehensive study of industry trends and competitor strategies."),
            ("KPI Framework", "Definition of key performance indicators for progress tracking."),
            ("Action Plan", "Step-by-step implementation guide for strategic initiatives.")
        ],
        "main_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200",
        "second_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200"
    },
    "digital-transformation.html": {
        "title": "Digital Transformation",
        "desc": "Modernize your business workflows and customer experience through innovative digital strategies. We provide the technology roadmap for your future growth.",
        "features": ["Cloud Migration Strategies", "Digital Customer Experience", "Data Analytics Integration", "Automation of Core Processes"],
        "docs": [
            ("Digital Audit", "Assessment of current technology stack and maturity."),
            ("Tech Roadmap", "Plan for implementing digital tools and systems."),
            ("Security Policy", "Framework for data protection in a digital environment."),
            ("Cloud Strategy", "Architecture for scalable and secure cloud operations.")
        ],
        "main_img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
        "second_img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200"
    },
    "risk-management.html": {
        "title": "Risk Management",
        "desc": "Identify and mitigate potential risks while ensuring complete regulatory compliance. Protect your business assets and reputation with our proven frameworks.",
        "features": ["Regulatory Compliance Audits", "Financial Risk Assessment", "Operational Security Plans", "Business Continuity Planning"],
        "docs": [
            ("Risk Register", "Comprehensive list of potential business risks and impacts."),
            ("Mitigation Plan", "Strategies for reducing or eliminating identified risks."),
            ("Compliance Audit", "Verification of adherence to industry regulations."),
            ("Continuity Plan", "Framework for maintaining operations during crises.")
        ],
        "main_img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1200",
        "second_img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?w=1200"
    },
    "business-process.html": {
        "title": "Business Process",
        "desc": "Streamline your operations and enhance value creation through process optimization. We help you eliminate waste and focus on what truly matters for your customers.",
        "features": ["Workflow Optimization", "Supply Chain Management", "Resource Efficiency", "Quality Assurance"],
        "docs": [
            ("Process Map", "Visual representation of current and future workflows."),
            ("Efficiency Report", "Analysis of resource usage and waste reduction."),
            ("QA Protocol", "Standards for maintaining product or service quality."),
            ("Supply Chain Plan", "Strategy for optimizing procurement and delivery.")
        ],
        "main_img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?w=1200",
        "second_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?w=1200"
    },
    "financial-management.html": {
        "title": "Financial Management",
        "desc": "Optimize your capital allocation and financial health. Our experts provide precise forecasting and budgeting tools to ensure long-term stability and growth.",
        "features": ["Capital Budgeting", "Financial Forecasting", "Audit Readiness", "Investment Planning"],
        "docs": [
            ("Financial Plan", "Comprehensive budget and investment strategy."),
            ("Forecast Report", "Projections for future revenue and expenses."),
            ("Audit Findings", "Detailed report on financial accuracy and compliance."),
            ("Investment Policy", "Guidelines for managing corporate capital.")
        ],
        "main_img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1200",
        "second_img": "https://images.unsplash.com/photo-1554224155-169745fe9a5c?w=1200"
    },
    "market-research.html": {
        "title": "Market Research",
        "desc": "Understand your market dynamics and competitor landscape with data-driven insights. We help you identify growth opportunities and customer needs.",
        "features": ["Consumer Insight Studies", "Market Trend Analysis", "Competitive Benchmarking", "Segmentation Strategy"],
        "docs": [
            ("Market Report", "In-depth analysis of industry size and growth."),
            ("Competitor Profile", "Study of rival strengths and weaknesses."),
            ("Customer Persona", "Detailed profile of target audience segments."),
            ("Trend Forecast", "Prediction of future market shifts and demands.")
        ],
        "main_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?w=1200",
        "second_img": "https://images.unsplash.com/photo-1551288049-bbbda536339a?w=1200"
    },
    "business-optimization.html": {
        "title": "Business Optimization",
        "desc": "Drive operational excellence across all levels of your organization. We identify performance gaps and implement strategies for superior business results.",
        "features": ["Performance Audits", "Change Management", "Talent Optimization", "Technology Alignment"],
        "docs": [
            ("Optimization Plan", "Strategy for improving business performance."),
            ("Gap Analysis", "Identification of areas for operational improvement."),
            ("Performance Metrics", "Key metrics for tracking business success."),
            ("Resource Map", "Plan for optimal allocation of business assets.")
        ],
        "main_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?w=1200",
        "second_img": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1200"
    },
    "it-consulting.html": {
        "title": "IT Consulting",
        "desc": "Modernize your IT infrastructure and align it with your business strategy. We provide expert guidance on software selection, security, and digital architecture.",
        "features": ["Infrastructure Design", "IT Security Audits", "Software Selection", "Tech Stack Strategy"],
        "docs": [
            ("IT Roadmap", "Plan for modernizing technology systems."),
            ("Security Audit", "Assessment of IT vulnerabilities and threats."),
            ("Tech Strategy", "Alignment of technology with business goals."),
            ("Software Plan", "Strategy for selecting and implementing software.")
        ],
        "main_img": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1200",
        "second_img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200"
    },
    "change-management.html": {
        "title": "Change Management",
        "desc": "Navigate organizational transitions smoothly with our expert change management strategies. We focus on cultural alignment and stakeholder communication.",
        "features": ["Stakeholder Engagement", "Cultural Readiness", "Training & Support", "Impact Assessment"],
        "docs": [
            ("Change Strategy", "Plan for managing organizational transitions."),
            ("Readiness Report", "Assessment of cultural and structural readiness."),
            ("Comm Plan", "Strategy for communicating change to stakeholders."),
            ("Training Roadmap", "Plan for building necessary employee skills.")
        ],
        "main_img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200",
        "second_img": "https://images.unsplash.com/photo-1517245327032-9792f6895c02?w=1200"
    },
    "leadership.html": {
        "title": "Leadership",
        "desc": "Develop the leadership skills necessary to drive organizational success. We provide executive coaching and strategic vision development for modern leaders.",
        "features": ["Executive Coaching", "Strategic Visioning", "Team Excellence", "Decision-making Training"],
        "docs": [
            ("Leadership Plan", "Strategy for developing executive capabilities."),
            ("Vision Statement", "Definition of corporate goals and purpose."),
            ("Team Audit", "Assessment of leadership team performance."),
            ("Coaching Roadmap", "Plan for ongoing leadership development.")
        ],
        "main_img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200",
        "second_img": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1200"
    },
    "growth-expansion.html": {
        "title": "Growth & Expansion",
        "desc": "Expand your business into new territories and markets with confidence. We provide the market analysis and scaling strategies for sustainable expansion.",
        "features": ["Market Entry Strategy", "Scalability Assessment", "Regional Expansion Plan", "Growth Forecasting"],
        "docs": [
            ("Growth Strategy", "Plan for expanding business operations."),
            ("Market Entry Plan", "Strategy for entering new territories."),
            ("Scalability Report", "Assessment of ability to manage growth."),
            ("Feasibility Study", "Analysis of potential for successful expansion.")
        ],
        "main_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200",
        "second_img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1200"
    }
}

def generate_page(filename, data):
    content = template_content
    # Page Title and Breadcrumb
    content = content.replace("<title>ABENTIS CONSULTING SL Business Consulting HTML Template</title>", f"<title>{data['title']} - ABENTIS CONSULTING SL</title>")
    content = content.replace('<h1 class="page_title">Service Details</h1>', f'<h1 class="page_title">{data["title"]}</h1>')
    content = content.replace('<span class="current">Service Details</span>', f'<span class="current">{data["title"]}</span>')

    # Content replacement
    features_html = "".join([f'<li><i class="pxni-checked"></i> {f}</li>' for f in data["features"]])
    docs_html = "".join([f'''
                    <div class="pxn_icon_box_2">
                      <div class="box_icon"><i class="pxni-checked-circle-2"></i></div>
                      <div class="box_content">
                        <h3 class="box_title">{title}</h3>
                        <div class="box_desc">{desc}</div>
                      </div>
                    </div>''' for title, desc in data["docs"]])

    inner_content = f'''
                  <h2>{data["title"]} Solutions</h2>
                  <p>{data["desc"]}</p>

                  <div class="row align-items-center row-gap-4 mt-30 mb-30">
                    <div class="col-12 col-md-6 col-lg-12 col-xl-6">
                      <img src="{data["main_img"]}" alt="Image">
                    </div>
                    <div class="col-12 col-md-6 col-lg-12 col-xl-6">
                      <h3>Professional Insights & Strategies</h3>
                      <ul class="pxn_list">
                        {features_html}
                      </ul>
                    </div>
                  </div>

                  <h2>Document Required</h2>
                  <div class="icon_box_wrap mb-30">
                    {docs_html}
                  </div>

                  <h2>Key Features</h2>
                  <ul class="pxn_list">
                    <li><i class="pxni-checked"></i> Our business consulting services are built to help organizations adapt and grow</li>
                    <li><i class="pxni-checked"></i> We combine strategic insight with deep industry expertise to deliver solutions</li>
                    <li><i class="pxni-checked"></i> From identifying growth opportunities to optimizing operations and guiding execution</li>
                    <li><i class="pxni-checked"></i> Our approach emphasizes clarity, collaboration, & measurable impact—ensuring strategies</li>
                  </ul>

                  <div class="mt-30 mb-30">
                    <img src="{data["second_img"]}" alt="Image">
                  </div>

                  <p>Our business consulting services help organizations strengthen performance, overcome challenges, & unlock sustainable growth. We work closely with businesses to understand their goals, analyze operations, and develop clear, actionable strategies. By combining industry expertise, data-driven insights, and hands-on execution support, we enable confident decision-making and deliver measurable results across strategy, operations.</p>

                  <div class="pxn_accordion_2 mt-30" id="pxnAccordion">
                    <div class="pxn_accordion_item_2">
                      <button class="accordion_question" type="button" data-bs-toggle="collapse"
                        data-bs-target="#pxnAccordion1" aria-expanded="true" aria-controls="pxnAccordion1">
                        1. What services do your business consultants provide?
                      </button>
                      <div id="pxnAccordion1" class="collapse show" data-bs-parent="#pxnAccordion">
                        <div class="accordion-body">
                          <div class="accordion_answer">
                            Our process typically starts with understanding your business goals, analyzing current operations, identifying challenges & opportunities, creating a tailored strategy. We then support implementation and track measurable outcomes.
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="pxn_accordion_item_2">
                      <button class="accordion_question collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#pxnAccordion2" aria-expanded="false" aria-controls="pxnAccordion2">
                        2. How does your consulting process work?
                      </button>
                      <div id="pxnAccordion2" class="collapse" data-bs-parent="#pxnAccordion">
                        <div class="accordion-body">
                          <div class="accordion_answer">
                            Our process typically starts with understanding your business goals, analyzing current operations, identifying challenges & opportunities, creating a tailored strategy. We then support implementation and track measurable outcomes.
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="pxn_accordion_item_2">
                      <button class="accordion_question collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#pxnAccordion3" aria-expanded="false" aria-controls="pxnAccordion3">
                        3. How long does a typical consulting engagement last?
                      </button>
                      <div id="pxnAccordion3" class="collapse" data-bs-parent="#pxnAccordion">
                        <div class="accordion-body">
                          <div class="accordion_answer">
                            Our process typically starts with understanding your business goals, analyzing current operations, identifying challenges & opportunities, creating a tailored strategy. We then support implementation and track measurable outcomes.
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="pxn_accordion_item_2">
                      <button class="accordion_question collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#pxnAccordion4" aria-expanded="false" aria-controls="pxnAccordion4">
                        4. What makes your consulting approach different?
                      </button>
                      <div id="pxnAccordion4" class="collapse" data-bs-parent="#pxnAccordion">
                        <div class="accordion-body">
                          <div class="accordion_answer">
                            Our process typically starts with understanding your business goals, analyzing current operations, identifying challenges & opportunities, creating a tailored strategy. We then support implementation and track measurable outcomes.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>'''
    
    # Surgical replacement of the INNER content of pxn_service_content
    # Find <h2>Explore our Service Lists</h2> and replace until the accordion's end
    start_mark = '<h2>Explore our Service Lists</h2>'
    end_mark = '</div>\n                  </div>\n                </div>\n              </div>' # This is tricky
    
    # Better: find pxn_service_content and replace its children but keep the div itself
    start_tag = '<div class="pxn_service_content">'
    end_tag = '</div>\n              </div>\n\n              <!-- sidebar -->'
    
    s_idx = content.find(start_tag) + len(start_tag)
    e_idx = content.find(end_tag)
    
    if s_idx != -1 and e_idx != -1:
        content = content[:s_idx] + inner_content + content[e_idx:]
    
    # Sidebar Active state
    sidebar_links = ""
    for f, d in services_data.items():
        active = "active" if f == filename else ""
        sidebar_links += f'''
                      <li>
                        <a class="service {active}" href="{f}">
                          <span class="service_title">{d["title"]}</span>
                          <span class="service_icon">
                            <span>
                              <i class="pxni-arrow-right"></i>
                              <i class="pxni-arrow-right"></i>
                            </span>
                          </span>
                        </a>
                      </li>'''
    
    content = re.sub(r'<ul class="pxn_services_list">.*?</ul>', f'<ul class="pxn_services_list">{sidebar_links}\n                    </ul>', content, flags=re.DOTALL)
    
    # Final cleanup
    content = content.replace("Read More", "")
    content = content.replace("Read more", "")
    
    return content

# Execute
for filename, data in services_data.items():
    page_html = generate_page(filename, data)
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(page_html)

print("All service pages re-generated with PERFECT layout preservation.")

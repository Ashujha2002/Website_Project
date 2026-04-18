import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
template_path = os.path.join(directory, 'blog-details.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

blog_data = {
    "strategic-growth-insights.html": {
        "title": "Strategic Growth Insights",
        "h2": "Unlocking Long-Term Business Potential",
        "author": "Marcus Thorne",
        "date": "10 Mar 2026",
        "category": "Strategy",
        "content_p1": "In today's volatile market, strategic growth is not just about increasing revenue; it's about building resilience and adaptability. Our latest analysis shows that firms focusing on sustainable expansion are 40% more likely to survive economic downturns.",
        "content_p2": "We explore the core pillars of growth: market penetration, product diversification, and operational agility. By aligning these elements with a clear corporate vision, leaders can navigate uncertainty with confidence.",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1200"
    },
    "digital-transformation-trends.html": {
        "title": "Digital Transformation Trends",
        "h2": "The Future of Digital Enterprise in 2026",
        "author": "Elena Rossi",
        "date": "22 Mar 2026",
        "category": "Technology",
        "content_p1": "Digital transformation has shifted from a competitive advantage to a fundamental necessity. From AI-driven automation to cloud-native architectures, the landscape is evolving faster than ever before.",
        "content_p2": "Our team breaks down the key technologies that are reshaping the consulting world. We look at how data-centric decision-making is empowering managers to optimize workflows and enhance customer satisfaction in real-time.",
        "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&q=80&w=1200"
    },
    "efficient-operations-guide.html": {
        "title": "Efficient Operations Guide",
        "h2": "Maximizing Productivity with Lean Methodologies",
        "author": "David Chen",
        "date": "05 Apr 2026",
        "category": "Operations",
        "content_p1": "Efficiency is the backbone of any successful organization. By eliminating waste and streamlining communication, businesses can significantly reduce overhead while increasing output quality.",
        "content_p2": "This guide provides practical steps for implementing Lean principles in a service-oriented environment. We discuss the importance of continuous feedback loops and the role of leadership in fostering a culture of operational excellence.",
        "img": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&q=80&w=1200"
    }
}

def generate_blog_page(filename, data):
    content = template_html
    # Titles
    content = content.replace('<title>ABENTIS CONSULTING SL Business Consulting HTML Template</title>', f'<title>{data["title"]} - ABENTIS CONSULTING SL</title>')
    content = content.replace('<h1 class="page_title">Blog Details</h1>', f'<h1 class="page_title">{data["title"]}</h1>')
    content = content.replace('<span class="current">Blog Details</span>', f'<span class="current">{data["title"]}</span>')
    
    # Content
    content = re.sub(r'<h2>How Strategic Planning Drives Long-Term Business Growth</h2>', f'<h2>{data["h2"]}</h2>', content)
    p_pattern = r'<p>Our business consulting blog is dedicated to sharing insights.*?inform\.</p>'
    content = re.sub(p_pattern, f'<p>{data["content_p1"]}</p><p>{data["content_p2"]}</p>', content, flags=re.DOTALL)
    
    # Image
    content = content.replace('./assets/images/blog/blog-standard-img-1.jpg', data["img"])
    
    # Meta
    content = re.sub(r'<span class="meta_text"><a href="#">Jessica Brown</a></span>', f'<span class="meta_text"><a href="#">{data["author"]}</a></span>', content)
    content = re.sub(r'<span class="meta_text"><a href="blog-details.html">Business</a></span>', f'<span class="meta_text"><a href="#">{data["category"]}</a></span>', content)
    
    return content

# Create files
for filename, data in blog_data.items():
    page_content = generate_blog_page(filename, data)
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(page_content)

# Update Nav
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
blog_links = "".join([f'<li><a href="{f}">{d["title"]}</a></li>' for f, d in blog_data.items()])
nav_pattern = r'<li class="has-dropdown[^"]*"><a href="[^"]*">Blog</a>\s*<ul class="sub-menu">.*?</ul>\s*</li>'
new_nav = f'<li class="has-dropdown"><a href="#">Blog</a><ul class="sub-menu">{blog_links}</ul></li>'

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    c = re.sub(nav_pattern, new_nav, c, flags=re.DOTALL)
    
    # Deep Image Scrub - Replace anything that looks like a broken local asset
    # Common broken patterns in this template
    c = c.replace('./assets/images/blog/post-thumb-img-1.jpg', 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&w=100&q=80')
    c = c.replace('./assets/images/blog/post-thumb-img-2.jpg', 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=100&q=80')
    c = c.replace('./assets/images/blog/post-thumb-img-3.jpg', 'https://images.unsplash.com/photo-1491975474562-1f4e30bc9468?auto=format&fit=crop&w=100&q=80')
    c = c.replace('./assets/images/blog/comment-avatar-1.jpg', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=50&q=80')
    c = c.replace('./assets/images/blog/comment-avatar-2.jpg', 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=50&q=80')
    c = c.replace('./assets/images/blog/comment-avatar-3.jpg', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=50&q=80')
    
    # Other miscellaneous broken assets
    c = c.replace('./assets/images/faq/h2-faq-cta-img.jpg', 'https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80')
    c = c.replace('./assets/images/services/h2-service-bg-img.jpg', 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80')
    
    # Handle footer portfolio link again just in case
    c = c.replace('href="blog.html"', f'href="{list(blog_data.keys())[0]}"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

print("3 Unique Blog pages created and Navigation/Images updated site-wide.")

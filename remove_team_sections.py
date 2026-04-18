import os
import re

directory = r'c:\Users\ashuj\OneDrive\Desktop\Abentis-consulting\html.pixeniumagency.com\rovix\demo'
all_html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Patterns to remove the Team section
team_section_patterns = [
    r'<!-- start: Team Section -->.*?<!-- end: Team Section -->',
    r'<section class="pxn-h1-team-section[^"]*">.*?</section>',
    r'<section class="pxn-h2-team-section[^"]*">.*?</section>',
    r'<section class="pxn-h3-team-section[^"]*">.*?</section>',
    r'<section class="pxn-team-section[^"]*">.*?</section>'
]

# Patterns to remove Team from navigation
nav_team_patterns = [
    r'<li><a href="team.html">Team</a></li>',
    r'<li><a href="team-details.html">Team Details</a></li>'
]

for filename in all_html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Team Sections
    for pattern in team_section_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)

    # 2. Remove Team from menus
    for pattern in nav_team_patterns:
        content = re.sub(pattern, '', content)

    # 3. Clean up empty sub-menus or orphaned tags if any (optional but good)
    # If the sub-menu becomes empty after removing Team, we might want to handle it, 
    # but usually "Pages" has more items (About, Pricing, etc.)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Delete team.html if it exists
team_file = os.path.join(directory, 'team.html')
if os.path.exists(team_file):
    os.remove(team_file)

print("Team sections and menu links removed from all pages.")

import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll replace the exact block of HTML using regex.
pattern = re.compile(r'[ \t]*<div class="toc-promo glass-panel">\s*<div class="promo-icon"><i class="fa-solid fa-rocket gradient-text"></i></div>\s*<h5>Ready to scale\?</h5>\s*<p>Book a demo with our growth team today\.</p>\s*<a href=".*?" class="btn-secondary btn-sm" target="_blank" rel="noopener noreferrer">Get Started</a>\s*</div>', re.DOTALL)

replacement = '                <ready-to-scale-promo></ready-to-scale-promo>'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if pattern matches
    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        print(f"Replaced in {f}")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

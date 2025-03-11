import markdown
import os
import shutil
import yaml
from pathlib import Path
from datetime import datetime

def parse_front_matter(content):
    """Extract YAML front matter from markdown content"""
    if content.startswith('---'):
        try:
            _, fm, content = content.split('---', 2)
            metadata = yaml.safe_load(fm)
            return metadata, content.strip()
        except:
            return {}, content
    return {}, content

def copy_assets(content_dir, output_dir):
    """Copy static assets to output directory"""
    # List of assets to check and copy
    assets = ['favicon.png', 'og-image.png']
    for asset in assets:
        src = content_dir / asset
        if src.exists():
            shutil.copy2(src, output_dir / asset)

def generate_site(content_dir="content", output_dir="public"):
    # Convert paths to Path objects
    content_dir = Path(content_dir)
    output_dir = Path(output_dir)
    
    # Create output directory and posts directory
    output_dir.mkdir(exist_ok=True)
    (output_dir / "posts").mkdir(exist_ok=True)

    # Copy static assets
    copy_assets(content_dir, output_dir)

    # HTML template with hamburger menu
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - LJLUG</title>
    <link rel="stylesheet" href="{css_path}terminal.css">
    <link rel="icon" type="image/png" href="{css_path}favicon.png">
    <meta property="og:title" content="{title} - LJ Linux Users Group">
    <meta property="og:description" content="LJ Linux Users Group - Supporting Linux and open source software">
    <meta property="og:image" content="{css_path}og-image.png">
    <meta property="og:type" content="website">
</head>
<body>
    <div class="nav-container">
        <div class="nav-brand">[<a href="index.html" style="color: black; text-decoration: underline;">lj university linux users group</a>] $</div>
        <button class="hamburger" onclick="toggleMenu()">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <nav class="nav-menu">
            <a href="{css_path}index.html">~/home</a>
            <a href="{css_path}about.html">~/about</a>
            <a href="{css_path}contact.html">~/contact</a>
            <a href="{css_path}posts.html">~/posts</a>
        </nav>
    </div>
    <div class="content">
        {content}
    </div>
    <footer>
        <!-- <p>© {year} LJ Linux Users Group. Powered by <a href="https://github.com/ljUlug">LJULUG</a>.</p>-->
        <p>website built using our very own vibe coded static site generator.</p>

    </footer>
    <script>
        function toggleMenu() {{
            document.querySelector('.nav-menu').classList.toggle('active');
            document.querySelector('.hamburger').classList.toggle('active');
        }}
    </script>
</body>
</html>"""

    # Create and write CSS
    with open(output_dir / "terminal.css", "w") as f:
        f.write("""
:root {
    --global-font-size: 15px;
    --global-line-height: 1.4em;
    --global-space: 10px;
    --font-stack: Menlo, Monaco, Lucida Console, Liberation Mono,
        DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace,
        serif;
    --mono-font-stack: Menlo, Monaco, Lucida Console, Liberation Mono,
        DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace,
        serif;
    --background-color: #222225;
    --page-width: 60em;
    --font-color: #e8e9ed;
    --invert-font-color: #222225;
    --secondary-color: #a3abba;
    --tertiary-color: #a3abba;
    --primary-color: #62c4ff;
    --error-color: #ff3c74;
    --progress-bar-background: #3f3f44;
    --progress-bar-fill: #62c4ff;
    --code-bg-color: #3f3f44;
    --input-style: solid;
    --display-h1-decoration: none;
}

* {
    box-sizing: border-box;
    text-rendering: geometricPrecision;
}

html {
    background-color: var(--background-color);
    color: var(--font-color);
    font-family: var(--font-stack);
    font-size: var(--global-font-size);
    line-height: var(--global-line-height);
}

body {
    margin: 0;
    padding: var(--global-space);
    max-width: var(--page-width);
    margin: 0 auto;
}

.nav-container {
    background-color: #ffd700;
    color: #000;
    padding: 10px 20px;
    margin: -10px -10px 20px -10px;
    font-family: var(--mono-font-stack);
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

.nav-brand {
    margin-right: 15px;
}

.nav-menu {
    display: flex;
    align-items: center;
}

.nav-menu a {
    color: #000;
    text-decoration: none;
    padding: 5px 10px;
}

.nav-menu a:hover {
    text-decoration: underline;
}

.hamburger {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 25px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    margin-left: auto;
}

.hamburger span {
    width: 100%;
    height: 3px;
    background-color: #000;
    transition: all 0.3s ease;
}

@media (max-width: 600px) {
    .hamburger {
        display: flex;
    }

    .nav-menu {
        display: none;
        width: 100%;
        flex-direction: column;
        align-items: flex-start;
        margin-top: 10px;
    }

    .nav-menu.active {
        display: flex;
    }

    .nav-menu a {
        width: 100%;
        padding: 10px 0;
    }

    .hamburger.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }

    .hamburger.active span:nth-child(2) {
        opacity: 0;
    }

    .hamburger.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -7px);
    }
}

.content {
    padding: 20px;
}

h1, h2, h3, h4, h5, h6 {
    margin-top: 2rem;
    color: var(--primary-color);
}

a {
    color: var(--primary-color);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

pre {
    background-color: var(--code-bg-color);
    padding: 1rem;
    overflow-x: auto;
}

code {
    background-color: var(--code-bg-color);
    padding: 0.2em 0.4em;
}

footer {
    margin-top: 40px;
    padding: 20px 0;
    border-top: 1px solid var(--secondary-color);
    text-align: center;
    color: var(--secondary-color);
}

.post-list {
    list-style: none;
    padding: 0;
}

.post-list li {
    margin-bottom: 20px;
}

.post-date {
    color: var(--secondary-color);
    font-size: 0.9em;
}""")

    # Process posts with front matter support
    posts = []
    posts_dir = content_dir / "posts"
    if posts_dir.exists():
        for post_file in posts_dir.glob("*.md"):
            with open(post_file, "r", encoding="utf-8") as f:
                content = f.read()
                metadata, content = parse_front_matter(content)
                
                # Skip draft posts
                if metadata.get('draft', False):
                    continue
                
                date_str = post_file.stem.split("-")[:3]
                try:
                    date = datetime.strptime("-".join(date_str), "%Y-%m-%d").strftime("%B %d, %Y")
                except:
                    date = "Unknown Date"
                
                title = metadata.get('title', " ".join(post_file.stem.split("-")[3:]).replace("-", " ").title())
                html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'codehilite'])
                
                # Save individual post
                post_html = html_template.format(
                    title=title,
                    content=html_content,
                    css_path="../",
                    year=datetime.now().year
                )
                
                output_post = output_dir / "posts" / f"{post_file.stem}.html"
                with open(output_post, "w", encoding="utf-8") as f:
                    f.write(post_html)
                
                posts.append({
                    "title": title,
                    "date": date,
                    "url": f"posts/{post_file.stem}.html"
                })

    # Generate posts index
    posts_list = "\n".join([
        f'<li><span class="post-date">{post["date"]}</span><br>'
        f'<a href="{post["url"]}">{post["title"]}</a></li>'
        for post in sorted(posts, key=lambda x: x["date"], reverse=True)
    ])
    
    posts_index = f"""
    <h1>Blog Posts</h1>
    <ul class="post-list">
        {posts_list}
    </ul>
    """
    
    with open(output_dir / "posts.html", "w", encoding="utf-8") as f:
        f.write(html_template.format(
            title="Posts",
            content=posts_index,
            css_path="",
            year=datetime.now().year
        ))

    # Convert regular pages with front matter support
    for md_file in content_dir.glob("*.md"):
        if md_file.stem in ["index", "about", "contact"]:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
                metadata, content = parse_front_matter(content)
                
                html_content = markdown.markdown(
                    content,
                    extensions=['fenced_code', 'tables', 'codehilite']
                )
                
                title = metadata.get('title', md_file.stem.replace("-", " ").title())
                
                final_html = html_template.format(
                    title=title,
                    content=html_content,
                    css_path="",
                    year=datetime.now().year
                )
                
                output_file = output_dir / f"{md_file.stem}.html"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(final_html)

    # Convert any additional markdown files in content directory
    for md_file in content_dir.glob("*.md"):
        if md_file.stem in ["index", "about", "contact"]:
            continue  # Skip files we've already processed
            
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        html_content = markdown.markdown(
            content,
            extensions=['fenced_code', 'tables', 'codehilite']
        )
        
        title = md_file.stem.replace("-", " ").title()
        
        final_html = html_template.format(
            title=title,
            content=html_content,
            css_path="",
            year=datetime.now().year
        )
        
        output_file = output_dir / f"{md_file.stem}.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_html)

if __name__ == "__main__":
    generate_site()
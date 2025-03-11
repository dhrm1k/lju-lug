# static site generator documentation

this is everything you need to know about setting up and using this static site generator.

## contents
1. project setup  
2. directory structure  
3. content creation  
4. local development  
5. github pages deployment  
6. customization  
7. troubleshooting  

## project setup

### initial setup

1. create the project directory:
   ```sh
   mkdir my-website
   cd my-website
   ```
2. set up a virtual environment:
   ```sh
   python -m venv venv
   ```
3. activate the virtual environment:
   ```sh
   # windows:
   venv\Scripts\activate
   # macos/linux:
   source venv/bin/activate
   ```
4. clone or copy these files into your project:
   - `static_site_generator.py`
   - `server.py`
   - `requirements.txt`
5. install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## directory structure

this is how the project should be structured:

```
my-website/
├── content/              # your markdown content
│   ├── posts/           # blog posts
│   ├── index.md         # homepage
│   ├── about.md         # about page
│   └── contact.md       # contact page
├── public/              # generated site
├── venv/                # virtual environment
├── static_site_generator.py
├── server.py
├── requirements.txt
└── .gitignore
```

create the required directories:
```sh
mkdir content
mkdir content/posts
mkdir public
```

## content creation

### creating pages

1. every markdown file follows this structure:
   ```md
   ---
   title: page title
   ---
   
   # main heading
   
   content goes here...
   ```
2. required pages (to be created in `content/`):
   
   **index.md**
   ```md
   ---
   title: home
   ---
   
   # welcome to our site
   
   main content here...
   ```
   
   **about.md**
   ```md
   ---
   title: about
   ---
   
   # about us
   
   about content here...
   ```
   
   **contact.md**
   ```md
   ---
   title: contact
   ---
   
   # contact us
   
   contact information here...
   ```

### creating blog posts

1. post naming convention:
   ```
   YYYY-MM-DD-post-title.md
   ```
2. example post (`content/posts/2024-01-15-first-post.md`):
   ```md
   ---
   title: first post
   ---
   
   # welcome to our blog
   
   this is our first blog post...
   ```

## local development

1. make sure the virtual environment is activated:
   ```sh
   # windows:
   venv\Scripts\activate
   # macos/linux:
   source venv/bin/activate
   ```
2. generate the site:
   ```sh
   python static_site_generator.py
   ```
3. start the local server:
   ```sh
   python server.py
   ```
4. visit `http://localhost:8000` in your browser
5. to make changes:
   - edit files in `content/`
   - run `static_site_generator.py` again
   - refresh your browser

## github pages deployment

1. create a `.gitignore` file:
   ```
   venv/
   __pycache__/
   .DS_Store
   ```
2. initialize git:
   ```sh
   git init
   git add .
   git commit -m "initial commit"
   ```
3. create a github repository and push the code:
   ```sh
   git remote add origin https://github.com/username/repo-name.git
   git branch -M main
   git push -u origin main
   ```
4. set up github pages:
   - go to repository settings
   - pages section
   - set source to github actions
5. create the deployment workflow:
   ```sh
   mkdir -p .github/workflows
   ```
   add a `.github/workflows/deploy.yml` file with the required content.

## customization

### changing colors

edit the `:root` section in `static_site_generator.py`:
```css
:root {
    --background-color: #222225;
    --font-color: #e8e9ed;
    --primary-color: #62c4ff;
    /* other colors... */
}
```

### modifying navigation

edit the `nav-menu` section in the html template inside `static_site_generator.py`:
```html
<nav class="nav-menu">
    <a href="{css_path}index.html">home</a>
    <!-- add/remove links -->
</nav>
```

## troubleshooting

### common issues and fixes

1. **module not found errors:**
   - check if the virtual environment is activated
   - run `pip install -r requirements.txt`
2. **pages not showing up:**
   - verify markdown files exist in `content/`
   - check file names and front matter
   - run `static_site_generator.py` again
3. **server issues:**
   - check if port `8000` is free
   - ensure you're in the right directory
   - verify `public/` directory exists
4. **deployment issues:**
   - check github repository settings
   - verify github actions is enabled
   - look at the actions tab for error logs

## quick reference

### common commands

1. setup:
   ```sh
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on windows
   pip install -r requirements.txt
   ```
2. development:
   ```sh
   python static_site_generator.py
   python server.py
   ```
3. git:
   ```sh
   git add .
   git commit -m "update message"
   git push
   ```
4. requirements:
   ```sh
   pip freeze > requirements.txt
   ```

### file locations
- **content:** `content/*.md`
- **posts:** `content/posts/*.md`
- **generated site:** `public/`
- **server:** `http://localhost:8000`

### reminders
- always work in the virtual environment
- regenerate the site after content changes
- test locally before pushing
- keep content backed up
- update `requirements.txt` when adding packages


### added later

## content formatting

when writing a post, you can now include the following front matter at the start of any markdown file:

```md
---
title: My Draft Post
draft: false
---
```

this allows you to specify a title and control whether the post is published or kept as a draft.

---
**end of documentation**

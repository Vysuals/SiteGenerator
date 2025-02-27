import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")

    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)

def extract_title(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                rel_path = os.path.relpath(md_path, dir_path_content)
                html_filename = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, html_filename)

                # Ensure destination directories exist
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)

                generate_page(md_path, template_path, dest_path)

if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

    CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
    TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "template.html")
    PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")

    generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, PUBLIC_DIR)

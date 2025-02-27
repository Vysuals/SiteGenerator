import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

# Get the base directory (SiteGenerator) path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Use absolute paths
dir_path_static = os.path.join(base_dir, "static")
dir_path_public = os.path.join(base_dir, "public")
dir_path_content = os.path.join(base_dir, "content")
template_path = os.path.join(base_dir, "template.html")


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # Ensure public directory exists
    os.makedirs(dir_path_public, exist_ok=True)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()

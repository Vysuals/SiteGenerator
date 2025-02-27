import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

# Get the base directory (SiteGenerator) path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Use absolute paths
dir_path_static = os.path.join(base_dir, "static")
dir_path_public = os.path.join(base_dir, "docs")
dir_path_content = os.path.join(base_dir, "content")
template_path = os.path.join(base_dir, "template.html")

# Get basepath from CLI argument or default to "/"
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # Ensure public directory exists
    os.makedirs(dir_path_public, exist_ok=True)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    # Replace this single page generation
    # generate_page(
    #     os.path.join(dir_path_content, "index.md"),
    #     template_path,
    #     os.path.join(dir_path_public, "index.html"),
    #     basepath
    # )

    # With the recursive function that generates all pages
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()

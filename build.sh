#!/bin/bash

# Ensure the script exits on the first error
set -e

echo "Building site for production..."

# Run the main Python script with the production basepath
python3 src/main.py "/SiteGenerator/"

echo "Build complete."

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 10:56:07 2025

@author: dakot
"""

import os
from pathlib import Path

# Path to repo root
repo_root = Path(__file__).parent
images_dir = repo_root / "images"

# Recursively find all .jpg files
image_paths = [
    str(path.relative_to(repo_root)).replace("\\", "/")
    for path in images_dir.rglob("*.jpg")
]

# Optional: sort or shuffle if you want a consistent order
# import random
# random.shuffle(image_paths)

# Build the HTML content
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Wedding Slideshow</title>
    <style>
        body {{
            margin: 0;
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <img id="slideshow" src="" alt="Slideshow">
    <script>
        const images = {image_paths};

        function shuffle(array) {{
            for (let i = array.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }}
        }}

        shuffle(images);

        let index = 0;
        const imgElement = document.getElementById("slideshow");

        function showNext() {{
            imgElement.src = images[index];
            index = (index + 1) % images.length;
        }}

        showNext();
        setInterval(showNext, 6000); // 3 seconds per image
    </script>
</body>
</html>
"""

# Write to index.html
with open(repo_root / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html created with", len(image_paths), "images.")

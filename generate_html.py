from pathlib import Path

repo_root = Path.cwd()
images_dir = repo_root / "images"

# Gather all .jpg and .jpeg files (recursively)
image_paths = []
for path in images_dir.rglob("*"):
    if path.suffix.lower() in [".jpg", ".jpeg"]:
        image_paths.append(str(path.relative_to(repo_root)).replace("\\", "/"))

# Generate the HTML with keyboard support
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

        function showImage(i) {{
            index = (i + images.length) % images.length;
            imgElement.src = images[index];
        }}

        function showNext() {{
            showImage(index + 1);
        }}

        function showPrevious() {{
            showImage(index - 1);
        }}

        showImage(index);

        let timer = setInterval(showNext, 6000);

        document.addEventListener("keydown", function(event) {{
            if (event.key === "ArrowRight") {{
                clearInterval(timer);
                showNext();
                timer = setInterval(showNext, 6000);
            }} else if (event.key === "ArrowLeft") {{
                clearInterval(timer);
                showPrevious();
                timer = setInterval(showNext, 6000);
            }}
        }});
    </script>
</body>
</html>
"""

# Write to index.html
with open(repo_root / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ index.html created with {len(image_paths)} images and keyboard support.")

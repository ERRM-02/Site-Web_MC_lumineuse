import html
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GALLERY_DIR = os.path.join(SCRIPT_DIR, "images", "galerie")
GALLERY_PAGE = os.path.join(SCRIPT_DIR, "galerie.html")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")


def rel_path(path):
    return os.path.relpath(path, SCRIPT_DIR).replace(os.sep, "/")


def build_gallery_items():
    items = []

    if not os.path.isdir(GALLERY_DIR):
        return items

    categories = [
        name for name in os.listdir(GALLERY_DIR)
        if os.path.isdir(os.path.join(GALLERY_DIR, name))
    ]

    for category in sorted(categories):
        category_dir = os.path.join(GALLERY_DIR, category)
        images = [
            name for name in os.listdir(category_dir)
            if name.lower().endswith(IMAGE_EXTENSIONS)
        ]

        for image_name in sorted(images):
            image_path = rel_path(os.path.join(category_dir, image_name))
            safe_category = html.escape(category)
            safe_path = html.escape(image_path, quote=True)
            items.append(f"""                <div class="gallery-page-item" data-lightbox="{safe_path}">
                    <img src="{safe_path}" alt="{safe_category} - réalisation ERRM" loading="lazy" />
                    <div class="gallery-page-overlay">
                        <span>{safe_category}</span>
                        <h3>Réalisation ERRM</h3>
                    </div>
                </div>""")

    return items


def update_gallery_page(items):
    with open(GALLERY_PAGE, "r", encoding="utf-8") as file:
        content = file.read()

    new_block = "\n".join(items)
    pattern = re.compile(
        r"(<!-- GALERIE_AUTO_START -->)(.*?)(<!-- GALERIE_AUTO_END -->)",
        re.DOTALL,
    )
    replacement = f"\\1\n{new_block}\n                \\3"
    updated = pattern.sub(replacement, content)

    with open(GALLERY_PAGE, "w", encoding="utf-8") as file:
        file.write(updated)


if __name__ == "__main__":
    gallery_items = build_gallery_items()
    update_gallery_page(gallery_items)
    print(f"{len(gallery_items)} photo(s) intégrée(s) dans galerie.html")

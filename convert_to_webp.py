import os
from PIL import Image

# Directories to search for images
image_dirs = [
    'static/assets/Project-Image',
    'static/assets/profile',
    'static/assets/certificates',
    'static/assets/experience-certificates'
]

# Supported extensions
exts = ('.jpg', '.jpeg', '.png')

def convert_image_to_webp(img_path):
    webp_path = os.path.splitext(img_path)[0] + '.webp'
    if os.path.exists(webp_path):
        return  # Skip if already converted
    try:
        img = Image.open(img_path).convert('RGB')
        img.save(webp_path, 'webp', quality=85)
        print(f'Converted: {img_path} -> {webp_path}')
    except Exception as e:
        print(f'Failed to convert {img_path}: {e}')

for d in image_dirs:
    for fname in os.listdir(d):
        if fname.lower().endswith(exts):
            convert_image_to_webp(os.path.join(d, fname)) 
import os
import io
from PIL import Image
from rembg import remove


valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')


def display_images(directory: str):
    """Displays all the images in a given directory"""
    images = [file for file in os.listdir(directory) if file.lower().endswith(valid_extensions)]
    if not images:
        print("No images found in the specified directory.")
    else:
        print("Images in the specified directory:")
        for img in images:
            print(img)


def remove_background(image_path: str, output_path: str):
    """Removes the background from the specified image."""
    try:
        with open(image_path, 'rb') as input_file:
            image_data = input_file.read()
            result = remove(image_data)
        img = Image.open(io.BytesIO(result)).convert("RGBA")
        img.save(output_path)
        print(f"Background removed and saved to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
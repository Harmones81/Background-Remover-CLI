import argparse
import os
from api import display_images, remove_background


def main():
    parser = argparse.ArgumentParser(description="Display images in a directory and remove the background of a specified image.")
    parser.add_argument('directory', type=str, help='The directory containing images.')
    parser.add_argument('--remove-bg', type=str, help='The image file name to remove background from (must be in the specified directory).')
    parser.add_argument('--output', type=str, help='The output file path for the image with the background removed.', default='output.png')

    args = parser.parse_args()

    # List all images in the directory
    display_images(args.directory)

    # If an image is specified for background removal, proceed with it
    if args.remove_bg:
        image_path = os.path.join(args.directory, args.remove_bg)
        if os.path.exists(image_path):
            remove_background(image_path, args.output)
        else:
            print(f"Image {args.remove_bg} not found in the specified directory.")


if __name__ == "__main__":
    main()
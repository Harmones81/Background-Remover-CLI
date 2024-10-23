# Background Remover CLI

A Python command-line tool to display all images in a user-specified directory and remove the background from a specified image using `rembg`.

## Features

- **List Images**: Display all images in a specified directory.
- **Remove Background**: Remove the background of a user-specified image and save the output.

## Prerequisites

- Python 3.7 or higher
- `rembg` library for background removal.

Install `rembg` using:
```bash
pip install rembg
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Harmones81/Background-Remover-CLI.git
cd Background-Remover-CLI
```

### Usage

1. **List all images in a directory**
   ```bash
   python main.py /path/to/your/directory
   ```
   This will display all images (PNG, JPG, JPEG, BMP, GIF) in the specified directory.
3. **Remove background from an image**
   ```bash
   python main.py -remove /path/to/your/image -output /path/to/your/output
   ```
   Replace `/path/to/your/image` with the image you want to process and `/path/to/your/output` with the path to save the output image with the background removed.


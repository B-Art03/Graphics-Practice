import os, sys
from PIL import Image
from pathlib import Path

palette = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

image_folder_path = Path(__file__).resolve().parents[2] / "images"

def main():
    try:
        with Image.open(image_folder_path / "IMG_7666.JPEG") as image:
            if image.mode != "RGB":
                image = image.convert("RGB")
            convert_to_ascii(image)

    except OSError:
        print("Error: Unable to open the image file. Please check the file path and format.")
    

def convert_to_ascii(image):
    image = image.convert("L")  # Convert to grayscale
    ascii_image = ""
    w, h = image.size
    
    for y in range(h):
        for x in range(w):
            pixel_value = image.getpixel((x, y))
            ascii_char = palette[round(pixel_value / (len(palette) * 10))]
            ascii_image += ascii_char
        ascii_image += "\n"
    
    # print(ascii_image)
    with open('b.txt', 'w') as f:
        f.write(ascii_image)


if __name__ == "__main__":
    main()
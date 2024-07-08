import PIL.Image
import argparse

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_characters = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    ascii_image = "".join(ascii_characters)
    return ascii_image

def main(args):
    try:
        image = PIL.Image.open(args.path)
    except Exception as e:
        print(f"Error: Unable to open image file {args.path}. {e}")
        return

    new_image_data = pixels_to_ascii(grayify(resize_image(image, args.width)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+args.width)] for i in range(0, pixel_count, args.width))

    print(ascii_image)

    if args.output:
        with open(args.output, "w") as f:
            f.write(ascii_image)
            print(f"ASCII art written to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("path", type=str, help="Path to the image file.")
    parser.add_argument("--width", type=int, default=100, help="Width of the ASCII art image.")
    parser.add_argument("--output", type=str, help="Output file (optional).")

    args = parser.parse_args()
    main(args)

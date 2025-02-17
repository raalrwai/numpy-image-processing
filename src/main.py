# src/main.py
from src.image_transformations import rgb_to_grayscale, apply_sepia, apply_negative
from src.utils import save_image, load_image

def main():
    input_image_path = "images/input_image.jpg"
    output_dir = "images/output/"

    # Load the image
    image_array = load_image(input_image_path)

    # Apply transformations
    grayscale_image = rgb_to_grayscale(image_array)
    sepia_image = apply_sepia(image_array)
    negative_image = apply_negative(image_array)

    # Save the transformed images
    save_image(grayscale_image, f"{output_dir}grayscale.jpg")
    save_image(sepia_image, f"{output_dir}sepia.jpg")
    save_image(negative_image, f"{output_dir}negative.jpg")

if __name__ == "__main__":
    main()
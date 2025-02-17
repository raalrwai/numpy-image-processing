# src/utils.py
from PIL import Image
import numpy as np

def load_image(image_path):
    """
    Load an image from the specified file path.
    Returns the image as a NumPy array.
    """
    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, output_path):
    """
    Save the NumPy array as an image to the specified path.
    """
    image = Image.fromarray(image_array)
    image.save(output_path)
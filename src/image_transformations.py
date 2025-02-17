# src/image_transformations.py
import numpy as np
from .utils import load_image, save_image

def rgb_to_grayscale(image_array):
    """
    Convert an RGB image to grayscale using the standard formula.
    """
    grayscale_array = np.dot(image_array[...,:3], [0.2989, 0.5870, 0.1140])
    return grayscale_array.astype(np.uint8)

def apply_sepia(image_array):
    """
    Apply a sepia filter to the image.
    """
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_image = np.dot(image_array[...,:3], sepia_filter.T)
    sepia_image = np.clip(sepia_image, 0, 255)
    return sepia_image.astype(np.uint8)

def apply_negative(image_array):
    """
    Apply a negative effect to the image by inverting pixel values.
    """
    return 255 - image_array
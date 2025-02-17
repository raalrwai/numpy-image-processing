Image Color Transformation Project
Overview
This project demonstrates various image color transformations such as RGB to grayscale, sepia, and negative. It leverages Python’s PIL library (Python Imaging Library) and basic image processing techniques to manipulate images. The transformations are applied to an image file, and the results are saved or displayed.

While the project is not deeply focused on AI, it utilizes foundational image processing techniques which are often used in AI-based image manipulation, such as pre-processing steps for deep learning models, style transfer, or image enhancement tasks.

Technologies Used
Python: The primary language for this project.
Pillow (PIL): A Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.
NumPy: A library for numerical computing, used to handle image data in array format.
Git: For version control and collaborating via GitHub.
How It Works
Grayscale Transformation: Converts a colored image into shades of gray, removing color information but keeping luminance details.
Sepia Transformation: Applies a vintage or warm tone to the image, often used for artistic effects.
Negative Transformation: Inverts the colors of the image, creating a "negative" of the original.
Each transformation is performed by manipulating pixel values in the image using NumPy arrays. The PIL.Image class handles loading and saving the images.

While not "AI" per se, image processing and transformation techniques like these are fundamental in the field of computer vision, which is a key area in AI.

How To Clone and Run Locally
Clone the repository

First, clone the repository to your local machine using the following command:

bash
Copy
git clone https://github.com/raalrwai/numpy-image-processing.git
Create and activate a virtual environment

Navigate to the project directory and create a virtual environment:

bash
Copy
cd numpy-image-processing
python3 -m venv venv
Then, activate the virtual environment:

On macOS/Linux:

bash
Copy
source venv/bin/activate
On Windows:

bash
Copy
venv\Scripts\activate
Install dependencies

Install the required dependencies by running:

bash
Copy
pip install -r requirements.txt
If requirements.txt is not available, you can install the necessary packages manually:

bash
Copy
pip install Pillow numpy
Run the project

After installing the dependencies, you can run the main script that applies image transformations:

bash
Copy
python src/main.py
Ensure that you have an image file (like input_image.jpg) in the images/ directory or adjust the path to your image.

Check Output

After running the script, you will find the transformed images in the same directory or the output folder (based on your script configuration).

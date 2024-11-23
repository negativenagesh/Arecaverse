import cv2
import numpy as np
from rembg import remove


def remove_background_in_memory(input_image):
    """
    Removes the background from an image using `rembg`.
    """
    _, buffer = cv2.imencode(".png", input_image)
    output_data = remove(buffer.tobytes())
    bg_removed_image = cv2.imdecode(np.frombuffer(output_data, np.uint8), cv2.IMREAD_UNCHANGED)
    return bg_removed_image


def process_arecanut_image_steps(input_image_path):
    """
    Processes the arecanut image step by step and returns intermediate results.
    """
    steps = {}

    # Read input image
    img = cv2.imread(input_image_path)
    if img is None:
        raise ValueError("Unable to read the input image.")

    steps["Original Image"] = img

    # Step 1: Remove Background
    bg_removed_img = remove_background_in_memory(img)
    steps["Background Removed"] = bg_removed_img

    # Step 2: Resize to 128x128
    resized_img = cv2.resize(bg_removed_img, (128, 128))
    steps["Resized Image (128x128)"] = resized_img

    # Step 3: Convert to Grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    steps["Grayscale Image"] = gray_img

    # Step 4: Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray_img)
    steps["CLAHE Enhanced Image"] = clahe_img

    # Step 5: Apply Sharpening
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(clahe_img, -1, sharpening_kernel)
    steps["Sharpened Image"] = sharpened_image

    # Step 6: Compute Sobel Gradient Magnitude
    sobelx = cv2.Sobel(sharpened_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(sharpened_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.hypot(sobelx, sobely)
    gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))
    steps["Sobel Gradient Magnitude"] = gradient_magnitude

    return steps
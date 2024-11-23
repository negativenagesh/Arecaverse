import cv2
import matplotlib.pyplot as plt
import os

def add_labels_to_images(input_folder, output_folder, label, font_scale=0.8, text_color=(255, 255, 255), bg_color=(0, 0, 0), thickness=2):
    """
    Adds a label to all images in the input folder and saves them in the output folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save labeled images.
        label (str): Text to be added as the label.
        font_scale (float): Scale of the font size.
        text_color (tuple): Color of the text in BGR format.
        bg_color (tuple): Background color for the text in BGR format.
        thickness (int): Thickness of the text.
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if not (filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg")):
            print(f"Skipping non-image file: {filename}")
            continue

        # Load the image
        image = cv2.imread(input_path)
        if image is None:
            print(f"Failed to load image: {filename}")
            continue

        # Resize the image for consistency
        resized_image = cv2.resize(image, (500, 500))  # Resize to 500x500 for demonstration purposes

        # Set font for the label
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Get text size to calculate the position
        (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, thickness)

        # Position the text at the bottom-left corner with padding
        text_x = 10  # Adjust this value for horizontal positioning
        text_y = resized_image.shape[0] - 10  # Place it near the bottom of the image

        # Add a black background rectangle for better text visibility
        cv2.rectangle(resized_image, (text_x, text_y - text_height - 5),
                      (text_x + text_width, text_y + baseline),
                      bg_color, -1)

        # Overlay the label text
        cv2.putText(resized_image, label, (text_x, text_y), font, font_scale, text_color, thickness)

        # Construct the output file path
        output_path = os.path.join(output_folder, filename)

        # Save the labeled image
        cv2.imwrite(output_path, resized_image)
        print(f"Labeled image saved: {output_path}")

    print("Processing complete. All labeled images are saved in the output folder.")

# Example Usage
input_folder = '/workspaces/Arecanut-quality-classification/image-preprocessing/preprocessed/preprocessed-1stchali'  # Replace with the path to your input folder
output_folder = '/workspaces/Arecanut-quality-classification/labels/1stchcali-labelled'  # Replace with the path to your output folder
label = 'I'  # Label to be added to all images

add_labels_to_images(
    input_folder=input_folder,
    output_folder=output_folder,
    label=label,
    font_scale=0.8,
    text_color=(255, 255, 255),  # White text
    bg_color=(0, 0, 0),  # Black background for text
    thickness=2
)
import os
import numpy as np
import pandas as pd
from PIL import Image

def images_to_dataframe(folder_path):
    
    flattened_images = []
    filenames = []
    image_names = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            image = Image.open(file_path)

            if image.size != (128, 128):
                raise ValueError(f"Image {filename} is not 128x128. Found size: {image.size}")
            
            flattened_image = np.array(image).flatten()

            flattened_images.append(flattened_image)
            filenames.append(filename)  
            image_names.append(os.path.splitext(filename)[0])
        
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    df = pd.DataFrame(flattened_images)

    df.columns = [f"Pixel-{i+1}" for i in range(16384)]

    df['filename'] = filenames
    df['image_name'] = image_names

    return df

if __name__ == "__main__":
    folder_path = "E:/arecanut/preprocessed-1stchali"

    df = images_to_dataframe(folder_path)

    print(f"DataFrame shape: {df.shape}")

    df.to_csv('1stchali.csv', index=False)

    print("DataFrame created and saved successfully!")


if __name__ == "__main__":
    folder_path = "E:/arecanut/preprocessed-gpre"

    df = images_to_dataframe(folder_path)

    print(f"DataFrame shape: {df.shape}")

    df.to_csv('gotu.csv', index=False)

    print("DataFrame created and saved successfully!")
    

if __name__ == "__main__":
    folder_path = "E:/arecanut/preprocessed-kole"

    df = images_to_dataframe(folder_path)

    print(f"DataFrame shape: {df.shape}")

    df.to_csv('kole.csv', index=False)

    print("DataFrame created and saved successfully!")
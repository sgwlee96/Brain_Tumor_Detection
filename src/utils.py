import os
import matplotlib.pyplot as plt
import cv2

def show_image(directory_path, num_images=9):
    """
    Display multiple images from a directory in a single figure
    
    Args:
    - directory_path (str): path to the img folder
    - num_images (int) : number of images to display. Base 9
    """
    files = os.listdir(directory_path)
    plt.figure(figsize=(12, 8))

    num_images_read = 0

    for img in files:
        file_path = os.path.join(directory_path, img)

        if os.path.isfile(file_path) and img.lower().endswith((".png", "jpg", "jpeg")):
            img = cv2.imread(file_path)

            if img is not None:
                num_images_read += 1

                plt.subplot(3, 3, num_images_read)
                plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                plt.axis("off")

                if num_images_read >= num_images:
                    break

    plt.tight_layout()
    plt.show()
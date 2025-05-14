# image_editor.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------------------
# Configuration
# -------------------------------
INPUT_IMAGE_PATH = 'test_cat.png'  # Replace with your image file name
OUTPUT_DIR = 'output_images'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -------------------------------
# Display image with matplotlib
# -------------------------------
def display_image(img, title, cmap=None):
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()


# -------------------------------
# Main Processing
# -------------------------------
def main():
    # Load image
    image = cv2.imread(INPUT_IMAGE_PATH)
    if image is None:
        print(f"❌ Error: Couldn't load image from {INPUT_IMAGE_PATH}")
        return
    print("✅ Image loaded successfully.")

    # Convert BGR to RGB for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image(image_rgb, "Original Image")

    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray_image, "Grayscale Image", cmap='gray')
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'grayscale_image.jpg'), gray_image)

    # Crop the image (rows 100–300, cols 200–400)
    cropped_image = image[100:300, 200:400]
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    display_image(cropped_rgb, "Cropped Region")
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'cropped_image.jpg'), cropped_image)

    # Rotate the image by 45 degrees
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
    display_image(rotated_rgb, "Rotated Image")
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'rotated_image.jpg'), rotated)

    # Increase brightness
    brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
    brighter = cv2.add(image, brightness_matrix)
    brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
    display_image(brighter_rgb, "Brighter Image")
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'brighter_image.jpg'), brighter)

    print("✅ All processing complete. Images saved in 'output_images/'.")


if __name__ == "__main__":
    main()

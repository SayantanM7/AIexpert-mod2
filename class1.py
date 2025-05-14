# image_resizer.py

import cv2
import os

def resize_and_save(image, size_name, dimensions, base_filename):
    """
    Resizes the image and saves it to disk.

    Args:
        image: Original image.
        size_name: Label for the resized image (e.g., 'small').
        dimensions: Tuple of (width, height).
        base_filename: Original filename without extension.
    """
    resized = cv2.resize(image, dimensions)
    output_filename = f"{base_filename}_{size_name}.jpg"
    
    cv2.imshow(f"{size_name.capitalize()} Image", resized)
    cv2.imwrite(output_filename, resized)
    
    print(f"✔ Saved {output_filename} ({dimensions[0]}x{dimensions[1]})")


def main():
    image_path = 'test_cat.png'  # Replace with your image file name
    base_filename = os.path.splitext(os.path.basename(image_path))[0]

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ Error: Unable to load image at '{image_path}'")
        return

    print("✅ Original image loaded successfully.")

    # Define target sizes
    sizes = {
        'small': (200, 200),
        'medium': (400, 400),
        'large': (600, 600)
    }

    # Resize and save
    for size_name, dimensions in sizes.items():
        resize_and_save(image, size_name, dimensions, base_filename)

    # Display images
    print("\n📸 Press any key in an image window to close all.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("👋 All windows closed. Done!")


if __name__ == "__main__":
    main()

import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Remove green
        filtered_image[:, :, 0] = 0  # Remove blue

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Remove green
        filtered_image[:, :, 2] = 0  # Remove red

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Remove blue
        filtered_image[:, :, 2] = 0  # Remove red

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image

# --- Load Image ---
image_path = 'test_cat.png'  # Make sure this file exists
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found! Please check the path.")
    exit()

# --- Instructions ---
print("🎨 Real-Time Color Filter Application")
print("Press the following keys to apply filters:")
print("  r - Red Tint")
print("  b - Blue Tint")
print("  g - Green Tint")
print("  i - Increase Red Intensity")
print("  d - Decrease Blue Intensity")
print("  o - Original Image")
print("  q - Quit")

filter_type = "original"  # Default to original image

while True:
    # Apply selected filter
    if filter_type == "original":
        filtered_image = image.copy()
    else:
        filtered_image = apply_color_filter(image, filter_type)

    # Show the filtered image
    cv2.imshow("Filtered Image", filtered_image)

    # Wait for key press
    key = cv2.waitKey(0) & 0xFF

    # Key mapping
    if key == ord('r'):
        filter_type = "red_tint"
    elif key == ord('b'):
        filter_type = "blue_tint"
    elif key == ord('g'):
        filter_type = "green_tint"
    elif key == ord('i'):
        filter_type = "increase_red"
    elif key == ord('d'):
        filter_type = "decrease_blue"
    elif key == ord('o'):
        filter_type = "original"
    elif key == ord('q'):
        print("👋 Exiting...")
        break
    else:
        print("⚠️ Invalid key! Use 'r', 'b', 'g', 'i', 'd', 'o', or 'q'.")

cv2.destroyAllWindows()

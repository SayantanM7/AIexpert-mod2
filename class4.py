import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Image in Grayscale
image = cv2.imread('test_cat.png', cv2.IMREAD_GRAYSCALE)

# 2. Apply Gaussian Blur to remove minor noise
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# 3. Apply Median Blur
median_blur = cv2.medianBlur(image, 5)

# 4. Apply Sobel Edge Detection (horizontal and vertical)
sobel_x = cv2.Sobel(gaussian_blur, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(gaussian_blur, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges

# Combine both directions
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# 5. Display Results
titles = ['Original', 'Gaussian Blur', 'Median Blur', 'Sobel X', 'Sobel Y', 'Sobel Combined']
images = [image, gaussian_blur, median_blur, sobel_x, sobel_y, sobel_combined]

plt.figure(figsize=(15, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

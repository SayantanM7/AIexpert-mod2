import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Unable to load image at {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def draw_regions_and_annotations(image_rgb):
    height, width, _ = image_rgb.shape

    # --- Rectangles ---
    rects = {
        "Region 1": ((20, 20), (170, 170), (0, 255, 255)),  # Yellow
        "Region 2": ((width - 220, height - 170), (width - 20, height - 20), (255, 0, 255))  # Magenta
    }

    centers = []
    font = cv2.FONT_HERSHEY_SIMPLEX

    for i, (label, (top_left, bottom_right, color)) in enumerate(rects.items(), start=1):
        cv2.rectangle(image_rgb, top_left, bottom_right, color, 3)
        center = ((top_left[0] + bottom_right[0]) // 2,
                  (top_left[1] + bottom_right[1]) // 2)
        centers.append((center, color))
        cv2.circle(image_rgb, center, 15, (0, 255, 0) if i == 1 else (0, 0, 255), -1)
        cv2.putText(image_rgb, label, (top_left[0], top_left[1] - 10), font, 0.7, color, 2, cv2.LINE_AA)
        cv2.putText(image_rgb, f'Center {i}', (center[0] - 40, center[1] + 40),
                    font, 0.6, (0, 255, 0) if i == 1 else (0, 0, 255), 2, cv2.LINE_AA)

    # --- Connecting line ---
    cv2.line(image_rgb, centers[0][0], centers[1][0], (0, 255, 0), 3)

    # --- Height arrow ---
    arrow_start = (width - 50, 20)
    arrow_end = (width - 50, height - 20)
    cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
    cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)
    height_label_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
    cv2.putText(image_rgb, f'Height: {height}px', height_label_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

    return image_rgb

def show_image(image_rgb, title="Annotated Image"):
    plt.figure(figsize=(12, 8))
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    image_path = 'test_cat.png'  # Replace with your image file name
    image_rgb = load_image(image_path)
    annotated = draw_regions_and_annotations(image_rgb)
    show_image(annotated)

if __name__ == "__main__":
    main()

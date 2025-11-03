import cv2
import numpy as np

def adjust_color_channels(image, r_scale, g_scale, b_scale):
    """Apply the RGB intensity adjustments to the image."""
    filtered = image.copy()

    filtered[:, :, 2] = np.clip(filtered[:, :, 2] * r_scale, 0, 255)  # Red channel
    filtered[:, :, 1] = np.clip(filtered[:, :, 1] * g_scale, 0, 255)  # Green channel
    filtered[:, :, 0] = np.clip(filtered[:, :, 0] * b_scale, 0, 255)  # Blue channel

    return filtered

image = cv2.imread("your_image.jpg")

if image is None:
    print("Error: Image not found. Please check file name.")
    exit()

r_scale = 1.2   
g_scale = 1.0   
b_scale = 0.8   

filtered_image = adjust_color_channels(image, r_scale, g_scale, b_scale)

cv2.imshow("Filtered Image", filtered_image)

import cv2
import numpy as np

IMAGE_FILE = "my_original_image.jpg" 

img = cv2.imread(IMAGE_FILE)

if img is None:
    print(f"Error: Could not load image from {IMAGE_FILE}. Check the file name and path.")
    exit()

(height, width) = img.shape[:2]

center_x, center_y = width // 2, height // 2

crop_size = 100
start_x = center_x - crop_size
end_x = center_x + crop_size
start_y = center_y - crop_size
end_y = center_y + crop_size


cropped_img = img[start_y:end_y, start_x:end_x]

rotation_angle = 45 
scale_factor = 1.0 
center = (width / 2, height / 2)
rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, scale_factor)

rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow("1. Original Image", img)
cv2.imshow("2. Cropped Image", cropped_img)
cv2.imshow("3. Rotated Image", rotated_img)


cv2.imwrite("output_cropped.jpg", cropped_img)
cv2.imwrite("output_rotated.jpg", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
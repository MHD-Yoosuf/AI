import cv2
import numpy as np


image_path = input("Enter the image file path: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges_canny = cv2.Canny(gray, 100, 200)
edges_sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
edges_laplacian = cv2.Laplacian(gray, cv2.CV_64F)

gaussian = cv2.GaussianBlur(image, (7, 7), 0)
median = cv2.medianBlur(image, 5)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge", edges_canny)
cv2.imshow("Sobel Edge", edges_sobel)
cv2.imshow("Laplacian Edge", edges_laplacian)
cv2.imshow("Gaussian Filter", gaussian)
cv2.imshow("Median Filter", median)

cv2.waitKey(0)
cv2.destroyAllWindows()

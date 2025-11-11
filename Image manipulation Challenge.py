import cv2
import numpy as np

image = cv2.imread('car.jpg')

if image is None:
    print("Error: Could not read the image" )
else:
    brightness_increase = 50
    brighter_image = cv2.add(image, brightness_increase)
    cv2.imwrite('brighter_image.jpg', brighter_image)
    
    print("Image processed successfully!")
    print("Original size:", image.shape)
    print("New image 'brighter_image.jpg' saved!")
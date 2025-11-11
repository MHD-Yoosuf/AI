import cv2

image_path = 'car.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}. Check the file path!")
else:
    size_small = (100, 100)
    size_medium = (300, 200)
    size_large = (640, 480)

    img_small = cv2.resize(image, size_small, interpolation=cv2.INTER_LINEAR)
    img_medium = cv2.resize(image, size_medium, interpolation=cv2.INTER_LINEAR)
    img_large = cv2.resize(image, size_large, interpolation=cv2.INTER_LINEAR)

    cv2.imshow('1. Small Image', img_small)
    cv2.imshow('2. Medium Image', img_medium)
    cv2.imshow('3. Large Image', img_large)

    cv2.imwrite('resized_small.jpg', img_small)
    cv2.imwrite('resized_medium.jpg', img_medium)
    cv2.imwrite('resized_large.jpg', img_large)

    print("Successfully created and saved three resized images!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
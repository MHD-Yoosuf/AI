import cv2

image_path = 'car.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}")
    print("Please check the file path.")
else:
    start_point = (50, 50)
    end_point = (250, 200)
    thickness = 2
    annotated_image = cv2.rectangle(image, start_point, end_point, color, thickness)
    
    
    cv2.imshow('Annotated Image', annotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
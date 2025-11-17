import cv2 
import numpy as np

def apply_filter(image,filter_type):

    if filter _type == "red tint":
        filter_image[:,:,1]=0
        filter_image[:,:,0]=0


    elif filter_type=="green tint":
        filter_image[:,:,0]=0 
        filter_image[:,:,2]=0

    elif filter_type =="blue tint":
        filter_image[:,:,1]=0
        filter_image[:,:,2]=0

    elif filter_type=="sobel":
        gray_image=cv2.Color(image,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
        sobely= cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3) 
        combined_sobel=cv2.bitwise_or(sobelx.astype('unit8'),sobely.astype('unit8'))
        filter_image=cv2.cvtColor(combined_sobel,cv2.COLOR_GRAY2BGR)

    elif filter_type=="canny":
        gray_image=cv2.Color(image,cv2.COLOR_BGR2GRAY) 
        edges=cv2.Canny(gray_image,100,200)
        filtered_image=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

    return filter_image 

image_path="car.jpg"   
image=cv2.imread(image_path)

if image is None:
    print("Error: image not found")


else:
    filter_type ="original"   

    print("Press the following keys to apply fiters:")
    print("r: Red Tint")
    print("g: Green Tint")
    print("b: Blue Tint")
    print("s: Sobel Edge Detection")
    print("c: Canny Edge Detection")
    print("q: Quit")

while True  :
    cv2.imshow("Image Filter Application",image)
    key=cv2.waitKey(0) & 0xFF

    if key== ord('r'):
        filter_type="red tint"
    elif key== ord('g'):
        filter_type="green tint"
    elif key== ord('b'):
        filter_type="blue tint"
    elif key== ord('s'):
        filter_type="sobel"
    elif key== ord('c'):
        filter_type="canny"
    elif key== ord('q'):
        break
    else:
        print("Invalid key pressed. Please try again.")

cv2.destroyAllWindows()
import cv2
import numpy as np 

def apply_color_filter(image,filter_type):
    filtered_image= image.copy()
    if filter_type="red_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,0]=0
    elif filter_type="blue tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0
    elif filter_type="green tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0
    elif filter_type="increase red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50) 
    elif filter_type="decrease_blue":
        filtered_image[:,:,0]=cv2.subtract(filtered_image[:,:,0]50)
    return filtered_image





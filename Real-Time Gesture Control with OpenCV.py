import cv2
import numpy as  np

cap=cv2.VideoCapture(0)
if not cap.isopened():
    print("Cannot open camera")
    exit()

 while True:
    ret,frame=cap.read()  

    if not ret:
        print("Error: Failed to capture image")
        break

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_skin=np.array([0,20,70],dtype=np.unit8)
    upper_skin=np.array([20,255,255],dtype=np.unit8)
    mask=cv2.inRange(hsv,lower_skin,upper_skin)

    result=cv2.inRange(hsv,lower_skin,upper_skin)

    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour=max(contours,key=cv2.contourArea)
        x,y,w,h=cv2.boundingRect(max_contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

       center_x=int(x+w/2)
       center_y=int(y+h/2)
       cv2.circle(frame,(center_x,center_y),5(0,0,225),1)

    cv2.imshow('Original Frame',frame) 
    cv2.imshow('Filtered Frame',result)

    if cv2.waitkey(1)  & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
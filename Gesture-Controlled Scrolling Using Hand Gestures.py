import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                lm_list.append([id, int(lm.x * w), int(lm.y * h)])


            thumb_tip = lm_list[4][2]
            index_tip = lm_list[8][2]


            if abs(thumb_tip - index_tip) > 60:
                pyautogui.scroll(20)
                cv2.putText(img, "Scrolling Up", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            else:
                pyautogui.scroll(-20)
                cv2.putText(img, "Scrolling Down", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("Hand Gesture Scrolling", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

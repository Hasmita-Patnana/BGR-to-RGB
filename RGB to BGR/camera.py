import cv2
import time

TIMER = int(5)    #Variable to store the countdown limit

cap = cv2.VideoCapture(0)
#Storing the input from the camera

while True:
    ret , img = cap.read()
    img1 = cv2.flip(img,1)
    cv2.imshow("a",img1)
    k = cv2.waitKey(125)
    if k == ord('c'):
        prev = time.time()

        while TIMER >= 0:
            ret , image = cap.read()
            img1 = cv2.flip(img,1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            

            cv2.putText(img1, TIMER ,(200,250), font, 7, (0,0,255),4, cv2.LINE_AA)
            cv2.imshow("a",img1)
            cv2.waitKey(125)

            cur = time.time()

            if cur - prev >=1:
                prev = cur
                TIMER = TIMER - 1

        else:
                ret , img = cap.read()
                img1 = cv2.flip(img,1)
            
                cv2.imshow("a",img1)
                cv2.waitKey(2000)
                cv2.imwrite("camera.jpg",img1)

    elif k == 27:
        break

cap.release()
cap.destroyAllWindows()        


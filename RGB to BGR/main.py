import cv2

img= cv2.imread(r"C:\Users\Hasmi\Downloads\Sixth-Sense-20211120T052756Z-001\Sixth-Sense\image.png",-1)

# -1 so it reads the image in BGR format

cv2.imshow("RGB image",img)

img1=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

cv2.imshow("BGR image",img1)

cv2.waitKey(10000)

cv2.destroyAllWindows()
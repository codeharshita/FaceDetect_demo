import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
#faceCascade = cv2.CascadeClassifier("Resouces/haarcascade_frontalface_default.xml") NOT USEFUL PARAMETERS.

img = cv2.imread('Resources/blackpink.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#To detect the faces we are gonna use this function.
faces = face_cascade.detectMultiScale(imgGray,1.1,4)

#creating a bounding box using for loop.
#To create the bounding box we need to get these four parameters.

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0), 2)
#(x,y) are initial points where (x+w), (y+h) are the corner points


cv2.imshow("Result", img)
cv2.waitKey(0)


import cv2

name = input("Enter your name here:")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(img,name,(x-1,y-1),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0))

    cv2.imshow('img', img)

    if cv2.waitKey(100) & 0xff == ord('q'):
        break

        cap.release()

        cv2.destroyAllWindows()

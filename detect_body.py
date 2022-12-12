import cv2

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

img = cv2.imread('./image/standing_people.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body = body_cascade.detectMultiScale(gray, 1.15, 5)

for (x, y, w, h) in body:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()


import numpy as np
import cv2 as cv

import paho.mqtt.client as mqtt

HOST="tx-broker"
PORT=1883
TOPIC="tx-face"

def on_connect(clnt, user, flags, rc):
    print("Connect with rc:" + str(rc))

face_client = mqtt.Client()
face_client.on_connect = on_connect
face_client.connect(HOST, PORT)

face_cascade = cv.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(1)

while(True):
    # Capture fxf
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]

        print("\nFace Detect Type: ", face.dtype)

        rc,png = cv2.imencode('.png', face)

        msg = png.tobytes()
        face_client.publish(TOPIC, payload=msg, qos=0, retain=False)
        print("Message Sent from Face Container!")

cv.destroyAllWindows()

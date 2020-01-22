import numpy as np
import cv2 as cv
import math

import paho.mqtt.client as mqtt

HOST = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "c-face"

path = "/data/"

index = 0

def on_connect(client, user, flags, rc):
    client.subscribe(TOPIC)
    print("Connected on rc: ", str(rc))

def on_message(client, userdata, msg):
    global path
    global index
    shipment = np.frombuffer(msg.payload, dtype="uint8")
    img = cv.imdecode(shipment, flags = 1)
    print("Received MSG: ", img.shape)
    s_name = "face_%s.png"%str(index)
    index += 1
    cv.imwrite(path+s_name, img)

cloud_client = mqtt.Client()
cloud_client.on_connect = on_connect
cloud_client.connect(HOST, PORT, 60)
print("Cloud Connect")
cloud_client.on_message = on_message
cloud_client.loop_forever()




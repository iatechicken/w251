# need to comment and fill R_HOST
import paho.mqtt.client as mqtt

HOST = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "tx-face"

R_HOST = "mqtt.eclipse.org"
R_PORT = 1883
R_TOPIC = "c-face"

def on_connect_local(client, userdata, flags, rc):
    print("Local Connect with rc: ", str(rc))
    client.subscribe(TOPIC)

def on_connect_remote(client, userdata, flags, rc):
    print("Remote Connect with rc: ", str(rc))

def on_message(client, userdata, msg):
    try:
        print("Got  Message!", msg)
        remote_mqttclient.publish(R_TOPIC, payload=msg.payload, qos=0, retain=False)
    except:
        print("Unexpected Error: ", sys.exe_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(HOST, PORT, 60)
print("Local Connect")
remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(R_HOST, R_PORT, 60)
print("Remote Connect")
local_mqttclient.on_message = on_message
local_mqttclient.loop_forever()

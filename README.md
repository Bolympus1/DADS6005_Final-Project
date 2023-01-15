# DADS6005_Final-Project
## Sentiment-Analysis 🌏

![Sentiment Analysis](https://user-images.githubusercontent.com/97329965/212549301-84b7ff20-add9-47d8-ad67-2bb78cab200c.png)

## 📝 Source code:publish
```python
import time
import pytchat
import json
import mysql.connector
from transformers import pipeline
from time import sleep
import paho.mqtt.client as paho
from paho import mqtt
from worldometer import Worldometer



def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set("Mekalone", "Watcharakorn007")

client.connect("e519cd77d46c464383728f1639fa2c4a.s1.eu.hivemq.cloud", 8883)

client.on_subscribe = on_subscribe
client.on_message = on_message  
client.on_publish = on_publish  




client.loop_start()

chat = pytchat.create(video_id="EBcvHK2Moys")

while chat.is_alive():
        for c in chat.get().sync_items():
            print(f'{c.datetime} {c.author.name} {c.message}')
            print(c.message)
            client.publish("youtubelive", payload=json.dumps(c.message, ensure_ascii=False).encode('utf8'), qos=1)
            #client.publish("youtubelive", payload=json.dumps(c.message), qos=1)
            #client.publish("youtubelive", payload=c.message, qos=1)


   
client.loop_stop()
```


![Sentiment Analysis (1)](https://user-images.githubusercontent.com/97329965/212549353-f2adb754-3559-4420-bb07-1a7669d86010.png)

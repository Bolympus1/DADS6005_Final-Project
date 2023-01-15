import time
import paho.mqtt.client as paho
from paho import mqtt
import mysql.connector
from transformers import pipeline
import requests



def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    insertMySql("youtube",str(msg.payload.decode()),sentiment(msg.payload.decode()))


def sentiment(message):
    classifier = pipeline('sentiment-analysis',model="poom-sci/WangchanBERTa-finetuned-sentiment")
    sentiment = classifier(message)
    mylist = sentiment[0]
    sentclass = mylist['label']

    return sentclass




def insertMySql(source,payloaddata,sentiment):

    cnx = mysql.connector.connect(user='sql6589589', password='DDFzTtZehi',
                              host='sql6.freesqldatabase.com',
                              database='sql6589589')

    cursor = cnx.cursor()

    ts = time.time()
    add_record = ("INSERT INTO realtimedata_yt "
                "( source, message, sentiment) "
                "VALUES ( '"+source+"', '"+str(payloaddata)+"','"+str(sentiment)+"')")
    

    # Insert new employee
    cursor.execute(add_record)
    
    cnx.commit()

    cursor.close()
    cnx.close()   
    print("Saved to Database") 


    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set("Mekalone", "Watcharakorn007")

client.connect("e519cd77d46c464383728f1639fa2c4a.s1.eu.hivemq.cloud", 8883)


client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish


client.subscribe("youtubelive", qos=1)

client.loop_forever()
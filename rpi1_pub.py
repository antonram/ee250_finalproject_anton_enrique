'''
Publish sound sensor information - RPi 1
'''

import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    # RPi doesn't subscribe to anything



if __name__ == '__main__':
    # connect to MQTT broker
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    # constantly get data and publish it
    while True:
        time.sleep(1)
        sound_data = False
        client.publish('rpi1/sound_sensor', sound_data)

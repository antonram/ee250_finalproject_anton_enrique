'''
Subscribe to both RPi sound sensor data
'''

import paho.mqtt.client as mqtt

import paho.mqtt.client as mqtt
import time

rpi1_values = []
rpi2_values = []

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe('rpi1/sound_sensor', 2)
    client.subscribe('rpi2/sound_sensor', 2)
    client.message_callback_add('rpi1/sound_sensor', rpi1_sound_callback)
    client.message_callback_add('rpi2/sound_sensor', rpi2_sound_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    pass

def rpi1_sound_callback(client, userdata, msg):
    print('RPi 1 Sound: ' + str(msg.payload, 'utf-8'))
    rpi1_values.append(msg.payload)

def rpi2_sound_callback(client, userdata, msg):
    print('RPi 2 Sound: ' + str(msg.payload, 'utf-8'))
    rpi2_values.append(msg.payload)

def remove_max(values):
    max = -1

def remove_min(values):
    min = 10000

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
        if len(rpi1_values) == 5 & len(rpi2_values) == 5:
            remove_max(rpi1_values)
            remove_max(rpi2_values)
            remove_min(rpi1_values)
            remove_min(rpi2_values)
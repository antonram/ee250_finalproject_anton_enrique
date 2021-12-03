'''
Publish sound sensor information - RPi 1
'''

import paho.mqtt.client as mqtt
import time
import requests
import sys
import affirmations_api

sys.path.append('/home/pi/Dexter/GrovePi/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd


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

    # Connect the Grove Sound Sensor to analog port A0
    # SIG,NC,VCC,GND
    sound_sensor = 0

    grovepi.pinMode(sound_sensor,"INPUT")

    CACHE = ['']*1
    CACHE[0] = '  ' + affirmations_api.AFFIRMATIONS_APP['init']() 
    ind = 0
    counter = 0 # will be to update affirmation every X amount of time
    LCD_LINE_LEN = 16

    lcd.setRGB(0,128,0)

    colors = [[128,128,128],[128,0,0],[0,128,128],[0,128,0],[0,0,128],[128,0,128],[32,95,128]]

    # constantly get data and publish it
    while True:
        try:
            sound_data = grovepi.analogRead(sound_sensor)
            client.publish('rpi1/sound_sensor', sound_data)
            
            if counter == 50:
                lcd.setText('TAKE A BREAK')
                CACHE[0] = ' ' + affirmations_api.AFFIRMATIONS_APP['init']()
                counter = 0
            lcd.setText_norefresh(CACHE[0][ind:ind+LCD_LINE_LEN])

            # ADDED SCROLL
            if ind < len(CACHE[0]):
                ind += 1
            else:
                ind = 0

            # print(CACHE[0]) <-- for debugging
            counter += 1
            # changes backlight to given color from color list (7 items)
            lcd.setRGB(colors[counter%7][0],colors[counter%7][1],colors[counter%7][2])
            time.sleep(.1)

        except IOError:
            print ("Error")

        except KeyboardInterrupt:
            # Gracefully shutdown on Ctrl-C
            lcd.setText('')
            lcd.setRGB(0, 0, 0)
            break

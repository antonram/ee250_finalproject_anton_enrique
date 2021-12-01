import time
import requests
import sys

sys.path.append('/home/pi/Dexter/GrovePi/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

grovepi.pinMode(sound_sensor,"INPUT")

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        # SEND VALUE TO COMPUTER

        # DELAY FOR NOW, CHECK MIN FOR SOUND SENSOR
        time.sleep(.05)

    except IOError:
        print ("Error")

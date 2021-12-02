import time
import requests
import sys
import affirmations_api

sys.path.append('/home/pi/Dexter/GrovePi/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

grovepi.pinMode(sound_sensor,"INPUT")

CACHE = ['']*1
CACHE[0] = '  ' + affirmations_api.AFFIRMATIONS_APP['init']() 
ind = 0

while True:
    try:
        # Read the sound level
	    sensor_value = grovepi.analogRead(sound_sensor)

        # SEND VALUE TO COMPUTER

        # DELAY FOR NOW, CHECK MIN FOR SOUND SENSOR
	    print("sexiness:", sensor_value)

	    # UPDATE CACHE TO CHANGE QUOTE
        CACHE[0] = '  ' + affirmations_api.AFFIRMATIONS_APP['init']()
	    
	    # DISPLAY API STUFF ON RPI
        # Comment out if you try to debug this on VM
	    lcd.setText.norefresh(CACHE[0][ind:ind+LCD_LINE_LEN])

        # ADDED SCROLL
	    if ind < len(CACHE[0]):
	        ind += 1
	    else:
	        ind = 0

      
       
	    print(CACHE[0])
	    time.sleep(.05)

    except IOError:
	    print ("Error")

    except KeyboardInterrupt:
	    # Gracefully shutdown on Ctrl-C
	    lcd.setText('')
	    lcd.setRGB(0, 0, 0)
	    break

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
counter = 0 # will be to update affirmation every X amount of time
LCD_LINE_LEN = 16

lcd.setRGB(0,128,0)

colors = [[128,128,128],[128,0,0],[0,128,128],[0,128,0],[0,0,128],[128,0,128],[32,95,128]]

while True:
    try:

    
        # Read the sound level
	    sensor_value = grovepi.analogRead(sound_sensor)


	    # UPDATE CACHE TO CHANGE QUOTE
	    if counter == 50:
			lcd.setText('TAKE A BREAK')
			ind = 0
        	CACHE[0] = ' ' + affirmations_api.AFFIRMATIONS_APP['init']()
	        counter = 0
	    # DISPLAY API STUFF ON RPI
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

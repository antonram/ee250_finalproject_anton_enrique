'''
Subscribe to both RPi sound sensor data
'''

import paho.mqtt.client as mqtt

import paho.mqtt.client as mqtt
import time

import matplotlib.pyplot as plt
# import matplotlib.animation as animation


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
    if len(rpi1_values) < 5:
        rpi1_values.append(int(msg.payload))

def rpi2_sound_callback(client, userdata, msg):
    print('RPi 2 Sound: ' + str(msg.payload, 'utf-8'))
    if len(rpi2_values) < 5:
        rpi2_values.append(int(msg.payload))

def remove_max(values):
    max = -1
    for i in range(len(values)):
        if int(values[i]) > int(max):
            max = values[i]
    values.remove(max)

def remove_min(values):
    min = 10000
    for i in range(len(values)):
        if int(values[i]) < int(min):
            min = values[i]
    values.remove(min)

'''
def animate(i, x, y, x_val, y_val, winner):
    x_val[-1] += 1
    y_val[-1] += winner
    print("ani winner:", winner)
    x.append(x_val[-1])
    y.append(y_val[-1])

    ax.clear()
    ax.plot(x,y)

    #plt.xticks(rotations=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Sexiness')
    plt.ylabel('Intensity')
'''

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    '''
    x = []
    y = []
    winner = 0
    x_val = [-1]
    y_val = [-1]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    counter = 0

    ani = animation.FuncAnimation(fig, animate, fargs=(x,y,x_val,y_val, winner), interval=1000)
    plt.show()
    '''
    progress = 0
    rounds = -1
    x = []
    y = []

    while True:
        time.sleep(1)
        if len(rpi1_values) >= 5 and len(rpi2_values) >= 5:
        #if len(rpi1_values) == 5:
            rounds += 1
            remove_max(rpi1_values)
            remove_max(rpi2_values)
            remove_min(rpi1_values)
            remove_min(rpi2_values)
            #print(rpi1_values)
            #print(rpi2_values)
            
            avg1 = sum(rpi1_values)/len(rpi1_values)
            avg2 = sum(rpi2_values)/len(rpi2_values)
            #avg2 = 5
            
            rpi1_values = []
            rpi2_values = []

            if avg1 > avg2:
                progress += 1
            elif avg2 > avg1:
                progress -= 1
            else:
                progress += 0
            y.append(progress)
            x.append(rounds)
        if progress == 5 or progress == -5:
            break
    plt.plot(x,y)
    plt.xlabel('time')
    plt.ylabel('progress')
    plt.show()



        
        
        
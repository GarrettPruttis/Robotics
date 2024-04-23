from time import *
from adafruit_servokit import ServoKit
from scipy.interpolate import interp1d
import keyboard
import time



kit = ServoKit(channels=16)


def setZero(angle):
    #if 130>=angle>=75:
    rangeConvert = interp1d([0, 180],[0,170])
    angle = rangeConvert(angle)
    kit.servo[0].angle = angle
def setOne(angle):
    #if 180>=angle>=0:
    kit.servo[1].angle = angle
def setTwo(angle):
    #if 180>=angle>=(140-angles[3]):
    kit.servo[2].angle = angle
def setThree(angle):
    #if 140>=angle>=0:
    kit.servo[3].angle = angle
def setFour(angle):
    #if 155>=angle>=90:
    print("original angle: ", angle)
    rangeConvert = interp1d([0, 180],[80,105])
    angle = rangeConvert(angle)
    print("mapped angle: ", angle)
    kit.servo[4].angle = angle
def setFive(angle):
    #if 170>=angle>=40:
    kit.servo[5].angle = angle
        
def setAngles(angles):
    setZero(angles[0])
    time.sleep(.1)
    setOne(angles[1])
    time.sleep(.1)
    setTwo(angles[2])
    time.sleep(.1)
    setThree(angles[3])
    time.sleep(.1)
    setFour(angles[4])
    time.sleep(.1)
    setFive(angles[5])

'''
angles = [80 , 180, 120, 50,  110, 100]
a =      [80 , 180, 120, 50,  110, 170]#good
b =      [80 , 180, 120, 50,  110, 170]#good
c =      [80 , 180, 100, 50,  110, 170]#good
d =      [130, 180, 100, 50,  110, 170]#good
e =      [130, 180, 100, 50,  110, 40]#good
f=       [130, 180, 100, 50,  110, 40]#good
g =      [80 , 180, 120, 50,  110, 40]#good ish
h =      [80 , 180, 120, 50,  110, 100]

setAngles([50,180,170,150,150,150])


while True:
    setAngles(angles)
    sleep(1)
    setAngles(a)
    sleep(1)
    setAngles(b)
    sleep(1)
    setAngles(c)
    sleep(1)
    setAngles(d)
    sleep(1)
    setAngles(e)
    sleep(1)
    setAngles(f)
    sleep(1)
    setAngles(g)
    sleep(1)
    setAngles(h)
    sleep(1)
    setAngles(g)
    sleep(1)
    setAngles(f)
    sleep(1)
    setAngles(e)
    sleep(1)
    setAngles(d)
    sleep(1)
    setAngles(c)49.59122388260938
    sleep(1)
    setAngles(b)
    sleep(1)
    setAngles(a)
    sleep(1)
    setAngles(angles)


run = True
current_key = 0
angles = [90,90,90,90,90,90]
while run:
    vel = 0
    
 
    if keyboard.is_pressed('a'):
        vel =-5
    elif keyboard.is_pressed('d'):
        vel += 5
    elif keyboard.is_pressed('x'):
        if current_key == 5:
            current_key =0
        else:
            current_key +=1
    elif keyboard.is_pressed('p'):
        run = False
    
    if current_key == 0:
        setZero(angles[0]+vel)
        angles[0] +=vel
    elif current_key == 1:
        setOne(angles[1]+vel)
        angles[1] +=vel
    elif current_key == 2:
        setTwo(angles[2]+vel)
        angles[2] +=vel
    elif current_key == 3:
        setThree(angles[3]+vel)
        angles[3] +=vel
    elif current_key == 4:
        setFour(angles[4]+vel)
        angles[4] +=vel
    elif current_key == 5:
        setFive(angles[5]+vel)
        angles[5] +=vel
    
        
        '''
        
    
    

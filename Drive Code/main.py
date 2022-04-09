import pygame
import RPi.GPIO as GPIO
import time

time.sleep(45)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Driving code for the robot
#
#

#pin setups

PIN_ARM_LEFT       = 3
PIN_ARM_RIGHT      = 5
PIN_BUCKET_LEFT    = 11
PIN_BUCKET_RIGHT   = 13
PIN_TRACK_LEFT     = 19
PIN_TRACK_RIGHT    = 21

GPIO.setup(PIN_ARM_LEFT, GPIO.OUT)
GPIO.setup(PIN_ARM_RIGHT, GPIO.OUT)
GPIO.setup(PIN_BUCKET_LEFT, GPIO.OUT)
GPIO.setup(PIN_BUCKET_RIGHT, GPIO.OUT)
GPIO.setup(PIN_TRACK_LEFT, GPIO.OUT)
GPIO.setup(PIN_TRACK_RIGHT, GPIO.OUT)

#SET PINS TO PWM
FREQUENCY = 150

PWM_ARM_LEFT            = GPIO.PWM(PIN_ARM_LEFT ,FREQUENCY)
PWM_ARM_RIGHT           = GPIO.PWM(PIN_ARM_RIGHT, FREQUENCY)
PWM_BUCKET_LEFT         = GPIO.PWM(PIN_BUCKET_LEFT ,FREQUENCY)
PWM_BUCKET_RIGHT        = GPIO.PWM(PIN_BUCKET_RIGHT, FREQUENCY)
PWM_TRACK_LEFT          = GPIO.PWM(PIN_TRACK_LEFT, FREQUENCY)
PWM_TRACK_RIGHT         = GPIO.PWM(PIN_TRACK_RIGHT, FREQUENCY)

DUTY_CYCLE_ARM = 50
DUTY_CYCLE_BUCKET = 50
DUTY_CYCLE_TRACK_LEFT = 50
DUTY_CYCLE_TRACK_RIGHT = 50

#start pwm signal
PWM_ARM_LEFT.start(DUTY_CYCLE_ARM)
PWM_ARM_RIGHT.start(DUTY_CYCLE_ARM)
PWM_BUCKET_LEFT.start(DUTY_CYCLE_BUCKET)
PWM_BUCKET_RIGHT.start(DUTY_CYCLE_BUCKET)
PWM_TRACK_LEFT.start(DUTY_CYCLE_TRACK_LEFT)
PWM_TRACK_RIGHT.start(DUTY_CYCLE_TRACK_RIGHT)

#pygame joysticks code
pygame.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for js in joysticks:
    js.init()
Left = 0
Right = 0
Arm = 0
Bucket = 0

offset = 0.0

exit1 = False

while not exit1:
    '''
    DUTY_CYCLE_ARM = 50
    DUTY_CYCLE_BUCKET = 50
    DUTY_CYCLE_TRACK_LEFT = 50
    DUTY_CYCLE_TRACK_RIGHT = 50
    
    
    
    '''
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
                Left = event.value 
            if event.axis == 4:
                Right = event.value
    
    
            '''
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
        if event.type == pygame.JOYBUTTONUP:
            print(event)
        if event.type == pygame.JOYHATMOTION:
            print(event)
            '''
    
    
    DUTY_CYCLE_TRACK_LEFT = int(16+0.1*(int(50-50*Left))) + offset
    DUTY_CYCLE_TRACK_RIGHT = int(16+0.1*(int(50-50*Right))) + offset
    
    '''
    PWM_ARM_LEFT.ChangeDutyCycle(DUTY_CYCLE_ARM)    #where 0.0 <= dc <= 100.0
    PWM_ARM_RIGHT.ChangeDutyCycle(DUTY_CYCLE_ARM)
    PWM_BUCKET_LEFT.ChangeDutyCycle(DUTY_CYCLE_BUCKET)
    PWM_BUCKET_RIGHT.ChangeDutyCycle(DUTY_CYCLE_BUCKET)
    '''
    PWM_TRACK_LEFT.ChangeDutyCycle(DUTY_CYCLE_TRACK_LEFT)
    PWM_TRACK_RIGHT.ChangeDutyCycle(DUTY_CYCLE_TRACK_RIGHT)
    

    #print(DUTY_CYCLE_TRACK_LEFT,DUTY_CYCLE_TRACK_RIGHT,'offset: ',offset)
    time.sleep(.2)
    #exit1= True
    
#STOP pwm signal
PWM_ARM_LEFT.stop()
PWM_ARM_RIGHT.stop()
PWM_BUCKET_LEFT.stop()
PWM_BUCKET_RIGHT.stop()
PWM_TRACK_LEFT.stop()
PWM_TRACK_RIGHT.stop()
    
pygame.joystick.quit()
pygame.quit()






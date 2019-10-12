import ASUS.GPIO as GPIO
import os
from subprocess import call
from time import sleep

# ****          Configuration           **** #
GpioMode                        = GPIO.ASUS
MotionSensor                    = 257
TimeUntilDisplayOff             = 10
# ****************************************** #

GPIO.setwarnings(False)
GPIO.setmode(GpioMode)
GPIO.setup(MotionSensor, GPIO.IN)

timer = TimeUntilDisplayOff

call(['xhost', '+'])
os.environ["DISPLAY"] = ":0.0"

try:
    while True:
        if GPIO.input(MotionSensor):
            timer = TimeUntilDisplayOff
            print ("Setting timer to  " + str(timer) + "s.")

        if timer > 0:
            timer -= 1
            print ("Timer: " + str(timer) + "s")

        else:
            print ("Timer is 0 -> turning display off.")
            call(['xrandr', '--output', 'HDMI-1', '--off'])

            GPIO.wait_for_edge(MotionSensor, GPIO.RISING)

            print ("Motion detected -> turning display on")
            call(['xrandr', '--output', 'HDMI-1', '--auto', '--rotate', 'left'])
            timer = TimeUntilDisplayOff

        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
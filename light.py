#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import requests

URL = "https://piflowertest.herokuapp.com"

# Read the pi's name from a config file
# That isn't include in the git repository
f = open("pi_name.txt", "r")
pi = f.read().strip()
print(pi)
f.close

LedPin = 17
BtnPin = 18
wasButtonPressed = "false"

def setup():
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
        GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
        # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def ready():
	i = 0
	while i < 3:
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(0.3)
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(0.3)
		i += 1

def pressButton(ev=None):
        global wasButtonPressed
        wasButtonPressed = "true"
        print("button pressed")
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LedPin, GPIO.HIGH)

def debug():
        GPIO.output(LedPin, GPIO.LOW)
        
def loop():
        # wait for falling and set bouncetime to prevent the
        #callback function from being called multiple times when the button is pressed
        global wasButtonPressed
        GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=pressButton, bouncetime=1000)
        while True:
                light = requests.get(URL+"/light?pi="+pi+"&button="+wasButtonPressed)
                response = light.json()
                if response["heardButtonPressed"]:
                        wasButtonPressed = "false"
                print(response)
                if response["shouldLight"] == True:
                        GPIO.output(LedPin, GPIO.LOW)
                        time.sleep(2)
                        GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(1)

def destroy():
        GPIO.output(LedPin, GPIO.HIGH)     # led off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        setup()
	ready()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

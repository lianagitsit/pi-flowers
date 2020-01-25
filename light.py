#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import requests

URL = "https://piflowertest.herokuapp.com"
pi = "liana"

LedPin = 17
BtnPin = 18

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	# Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
	print("button pressed")
	requests.get(URL+"/button?pi="+pi)

def loop():
	# wait for falling and set bouncetime to prevent the
        #callback function from being called multiple times when the button is pressed
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed, bouncetime=1000)
	while True:
		light = requests.get(URL+"/light?pi="+pi)
		response = light.json()
		print(response)
		if response["shouldLight"] == True:
			GPIO.output(LedPin, GPIO.LOW)
			time.sleep(1)
			GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(2)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

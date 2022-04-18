#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
from time import sleep

def readTemperature():
    # Reading CPU temprature
    readTemp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    # Convert the read temperature into integer, to the correct format and to integer
    readTemp = int(int(readTemp) / 1000)

    return readTemp

# Initialisation of the while-loop
x = 1

while x > 0:
    # GEt the temperature
    temperatur = readTemperature()

    # debuging
    #print(temperatur)

    # Set the pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    # debuging
    #print("Start while")

    # If the temperatur under 55 °C
    if temperatur <= 55:
        GPIO.output(11, GPIO.LOW)

        # Delete the pin set
        GPIO.cleanup()

        # debuging
        #print("under 55")

        # Programm timeout for five minute
        sleep(300)

    # Else temperature over 55 °C
    else:
        GPIO.output(11, GPIO.HIGH)

        # debuging
        #print("over 55")

        # Programm timeout for five minute
        sleep(300)

        # Delete the pin set
        GPIO.cleanup()

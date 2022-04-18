#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
from time import sleep

def readTemperature():
    # Auslesen der Temperatur der CPU
    readTemp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    # Umwandeln der ausgelesenen Temperatur von string in integer, ins richtige
    # Format und von float in integer
    readTemp = int(int(readTemp) / 1000)
    return readTemp

# Initialisierung der While-Schleife
x = 1

while x < 10:
    # Einlesen der Temperatur
    temperatur = readTemperature()

    # debuging
    #print(temperatur)

    # Pin Belegung festlegen
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    # debuging
    #print("Start while")

    # Temperatur unter 55°C ist der Lüfter aus
    if temperatur <= 55:
        GPIO.output(11, GPIO.LOW)

        # Löschen der Pin Belegung da der Ausgang nicht vollständig abschaltet
        GPIO.cleanup()

        # debuging
        #print("unter 55")

        # Fünf Minuten Pause bis die Temperatur erneut geprüft wird
        sleep(300)

    # Temperatur über 55°C ist der Lüfter an
    else:
        GPIO.output(11, GPIO.HIGH)

        # debuging
        #print("über 55")

        # Fünf Minuten Pause bis die Temperatur erneut geprüft wird
        sleep(300)

        # Aus sicherheitsgründen wird vor dem erneuten Prüfen der Temperatur,
        # die Pin Belegung gelöscht
        GPIO.cleanup()

#! /usr/bin/python3
import wiringpi
import time
wiringpi.wiringPiSetupGpio()

MOTOR_PIN_1 = 11
DIR_PIN_1 = 10
MOTOR_PIN_2 = 19
DIR_PIN_2 = 13
MOTOR_PIN_3 = 6
DIR_PIN_3 = 5

motor_pin = MOTOR_PIN_3
dir_pin = DIR_PIN_3

wiringpi.softToneCreate(motor_pin)
wiringpi.softToneCreate(dir_pin)

hz = 440
x = True
while x:
    tex = input("d, u, q vagy hz: ")
    try:
        hz = int(tex)
    except:
        if tex == "d":
            hz -= 1
        elif tex == "u":
            hz += 1
        elif tex == "q":
            x = False
    wiringpi.softToneWrite(motor_pin, hz*2)
    wiringpi.softToneWrite(dir_pin, hz)

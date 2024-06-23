#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:47:43 2024

@author: pi
"""
import sys
import RPi.GPIO as GPIO
import time

def alloff():
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

mag,mode = sys.argv[1],sys.argv[2]

t = 5.0

if mag == 'soft':
    f = 5
if mag == 'medium':
    f = 3
if mag == 'hard':
    f = 1
        
if mode == "pat":
    for i in range (int(f*t)):
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        time.sleep (1.0/f)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        time.sleep (1.0/f)
        
if mode == "jab":
    for i in range (int(f*t)):
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep (1.0/f)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        time.sleep (1.0/f)


if mode == "tickle":
    for i in range (int(f*t)):
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        time.sleep (1.0/f)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        time.sleep (1.0/f)
    alloff()
    
if mode == "squeeze":
    for i in range (int(f*t)):
        alloff()
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        time.sleep (0.66/f)
        alloff()
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(32, GPIO.HIGH)
        time.sleep (0.66/f)
        alloff()
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep (0.66/f)

    alloff()
    
if mode == "slap":
    for i in range (int(f*t)):
        alloff()
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        time.sleep (0.4/f)
        alloff()
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        time.sleep (0.4/f)
        alloff()
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep (0.4/f)
        alloff()
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(32, GPIO.HIGH)
        time.sleep (0.4/f)
        alloff()
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        time.sleep (0.4/f)
    alloff()

GPIO.cleanup()

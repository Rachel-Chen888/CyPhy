# Copyright (c) 2025, BlackBerry Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from turtle import setup
import rpi_gpio as GPIO  # Import the QNX Raspberry Pi GPIO module for controlling GPIO pins
import time  # Import the time module for adding delays
 
# Set GPIO pins as an output pin
def setup():
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

# Initially set GPIO pins to LOW (turning it OFF) 
def turnOffAll():
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    
turnOffAll()  # Turn LED OFF initially
    
# Initially set GPIO pins to HIGH (turning it ON) 
def turnOnAll():
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)

# Infinite loop to blink the LED
while True:
    turnOnAll()  # Turn LED ON
    time.sleep(0.5)  # Wait for 0.5 seconds

    turnOffAll()  # Turn LED OFF
    time.sleep(0.5)  # Wait for 0.5 seconds
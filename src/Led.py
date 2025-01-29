from machine import Pin
import time

# Allumage de la LED exterieure

led = Pin(16, Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
    
import time
from machine import Pin

# Hello World Roar Hunter
n=0
led = Pin("LED", Pin.OUT)
while True:
    print(f"Hello Word {} \n",n)
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(0.5)
    n+=1
    
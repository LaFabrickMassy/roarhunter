from machine import Pin
import time

# Allumage de la barre LED avec le registre a decalalage


# PIN 11	SH_CP	Shift register clock pin => GP2
# PIN 12	ST_CP	Storage register clock pin (latch pin) => GP1
# PIN 14	DS	Serial data input => GP0



clock = Pin(2, Pin.OUT)
latch = Pin(1, Pin.OUT)
data_input = Pin(0, Pin.OUT)

led = Pin("LED", Pin.OUT)
latch.value(0)

while True:
    for i in range(0, 4):
        data = 0
        if i==0:
            data = 1
        latch.value(0)
        data_input.value(data) 
        clock.value(1)
        data_input.value(0)
        latch.value(1)
        time.sleep(0.5)
        clock.value(0)      
        led.toggle()
        
    
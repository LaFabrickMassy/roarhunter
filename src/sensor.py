from machine import ADC
import time

adc = ADC(26)

while True:
    value = adc.read_u16()
    print(f"value:{}", value)
    time.sleep(1)
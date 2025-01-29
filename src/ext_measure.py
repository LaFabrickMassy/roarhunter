from machine import Pin
import time
from machine import ADC

# mesure d'un signal exterieur du potentiometre

# PIN31 = GP26 pour le port analogique

signal = ADC(Pin(26))
while True:
    val = signal.read_u16()   # read an analog value in microvolts
    
    print(f"valeur={val}")
    time.sleep(1)


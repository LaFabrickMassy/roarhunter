from machine import Pin, I2C
import time
from machine import ADC
from ssd1306 import SSD1306_I2C

# mesure d'un signal exterieur du potentiometre
# affichage sur l ecran oled

seuil_alarm = 1.5 # en volt
tempo_alarm = 2000 # en ms

# PIN31 = GP26 pour le port analogique
WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14)) # Init I2C using I2C0 defaults,
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

signal = ADC(Pin(26)) # potentiometre
alarm = Pin(11,Pin.OUT) # led
t0 = time.ticks_ms()
while True:
    val = signal.read_u16()   # read an analog value in microvolts
    voltage = val*3.3/(1<<16)
    # print(f"valeur={val}")
    oled.fill(0)
    texte=str(f"Volt= {voltage:.2f}V")
    oled.text(texte ,5,32)
    oled.show()
    if voltage>1.5:
        alarm.value(1)
        t0 = time.ticks_ms() # temps au moment du changement d'etat
    
    if (time.ticks_ms()-t0)>tempo_alarm: # hysteresis temporelle pour empecher le chgt d etat intepestif
        alarm.value(0)
    time.sleep(0.1)


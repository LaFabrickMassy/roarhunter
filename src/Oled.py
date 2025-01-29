from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14)) # Init I2C using I2C0 defaults,
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
n=0
while True:
    oled.fill(0)
    texte=str(f"Hello {n}")
    oled.text(texte ,5,32)
    oled.show()
    n+=1
    time.sleep(1)

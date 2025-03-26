from machine import Pin
import time
from machine import ADC

# Allumage de la barre LED avec le registre a decalalage


# PIN 11	SH_CP	Shift register clock pin => GP2
# PIN 12	ST_CP	Storage register clock pin (latch pin) => GP1
# PIN 14	DS	Serial data input => GP0
# PIN 31 = GP26 pour le port analogique pour le potentiometre
adc = ADC(Pin(26))


clock = Pin(2, Pin.OUT)
latch = Pin(1, Pin.OUT)
data_input = Pin(0, Pin.OUT)

led = Pin("LED", Pin.OUT)
latch.value(0)


def send_value(value):
    latch.value(0)
    for i in range(31, -1,-1):
        clock.value(0)
        bit=value>>i&1
        data_input.value(bit)
        clock.value(1)
        #print((i,bit))
    latch.value(1)
# send_value(450213)

def compute_into_bit_number(value):
    number_of_bits =  value >> 11
    return number_of_bits

def set_bits(n):
    result=0
    for i in range (n):
        result |= 1<<i
        # print(f"result={result}")
    return result

while True:
    val = adc.read_u16()   # read an analog value in microvolts
    voltage = val*3.3/(1<<16) # 3,3V et 1<<16 est la valeur max
    # print(f"voltage={voltage}")
    
    nbbit = compute_into_bit_number(val)
    # print(f"nb bit={nbbit}")
    ledvalues=set_bits(nbbit)
    send_value(ledvalues)
    # print(f"led value={ledvalues}")
    time.sleep(0.1)
    
        
    
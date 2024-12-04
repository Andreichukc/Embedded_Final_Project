import machine
from time import sleep
from EMF_Lights_class import Lights
from magnometer import magnometer_sensor

meter = magnometer_sensor()
leds = Lights()

while(True):
    EMF = meter.read()
    
    leds.toggle_lights(EMF)
    sleep(.5)
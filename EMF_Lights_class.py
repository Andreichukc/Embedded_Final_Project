import machine
from time import sleep

red = machine.Pin(6, machine.Pin.OUT)
yellow2 = machine.Pin(5, machine.Pin.OUT)
yellow1 = machine.Pin(4, machine.Pin.OUT)
green2 = machine.Pin(3, machine.Pin.OUT)
green1 = machine.Pin(2, machine.Pin.OUT)
buzzer = machine.Pin(7, machine.Pin.OUT)

red.value(0)
yellow2.value(0)
yellow1.value(0)
green2.value(0)
green1.value(1)


class Lights:
    def __init__(self):
        self.emf = 0
        
    def toggle_lights(self, emf):
        self.emf = emf
        print(emf)
        green1.value(1)
        if emf > 91000:
            green2.value(1)
            buzzer.value(1)
        else:
            buzzer.value(0)
            green2.value(0)
            
        if emf > 95000:
            yellow1.value(1)
        else:
            yellow1.value(0)
        if emf > 98000:
            yellow2.value(1)
        else:
            yellow2.value(0)
                
        if emf > 110000:
            red.value(1)
        else:
            red.value(0)
        
# leds = Lights()
# 
# leds.toggle_lights(1)

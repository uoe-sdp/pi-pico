import machine
from time import sleep
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
sleep (1)
led.off()
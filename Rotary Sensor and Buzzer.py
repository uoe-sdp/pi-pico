from machine import Pin,PWM,ADC
from time import sleep
adc = ADC(0) #ADC input (knob potentiometer) connected to A0
pwm = PWM(Pin(27))#DAC output (buzzer) connected to A1
pwm.freq(10000)
while True:
    
    '''Analog port test'''
    val = adc.read_u16()#Read A2 port adc value (65535~0)
    #Drive the buzzer, turn off the buzzer when the adc value is less than 300
    if val > 300:
        pwm.freq(int(val/10))
        pwm.duty_u16(10000)
    else:
        pwm.duty_u16(0)
    print(val)
    sleep(0.05)
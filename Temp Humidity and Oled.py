from ssd1306 import SSD1306_I2C
from dht20 import DHT20
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht11 import *
from machine import Pin, I2C
from time import sleep

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=200000)#oled connect to I2C1
oled = SSD1306_I2C(128, 64, i2c)
dht2 = DHT(18) #temperature and humidity sensor connect to D18 port


while True:  

    temp,humid = dht2.readTempHumid()#temp:  humid:
    '''I2C port test'''    
    ''' oled display test'''
    oled.fill(0)#Clear screen
    oled.text("Temp:  " + str(temp),0,0)#display tempearture on line 1
    oled.text("Humid: " + str(humid),0,8)
    oled.show()
    sleep(0.5)
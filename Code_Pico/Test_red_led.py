from machine import Pin
import time
led_rouge = Pin(15, Pin.OUT)
led_blue = Pin(14, Pin.OUT)
while True:
 led_rouge.toggle()
 time.sleep(0.5)
 led_blue.toggle()
 time.sleep(0.5)
 
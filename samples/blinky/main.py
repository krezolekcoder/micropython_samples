import sys
from machine import Pin, Timer

led = Pin('LED', Pin.OUT)
gpio = Pin(1, Pin.OUT)

timer = Timer()

def blink(timer):
    led.toggle()
    gpio.toggle()

timer.init(freq=1.0, mode=Timer.PERIODIC, callback=blink)

if __name__ == "__main__":

    print("Hello world from rpi 2350W ")

    print(sys.implementation)

 
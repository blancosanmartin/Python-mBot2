import cyberpi, mbuild
from time import sleep

for x in range(0,16):
    for y in range(0,8):
        #                          x  y  value (True = 1, False = 0)
        mbuild.led_panel.set_pixel(x, y, True, 1)
        sleep(0.1)

mbuild.led_panel.clear(1)

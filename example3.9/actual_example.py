#!/usr/bin/env python

import opc

led_colour=[(255,0,0)]*10

client = opc.Client('localhost:7890')
print (enumerate(led_colour))
for item in enumerate(led_colour):
    print (item)
    if item[0]==5:
        #need to get values out of tuple
        r, g, b = item[1]
        r = 0
        g = 255

        #create changed tuple (uses some values from old and some new) 
        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour

client.put_pixels(led_colour)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
print (led_colour)
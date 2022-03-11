#!/usr/bin/env python3

fb=1

while fb <= 100:
    if 0 == fb % 3 and fb % 5:
        print(fb, "fizzbuzz")
    elif 0 == fb % 3:
        print(fb, "fizz")
    elif 0 == fb % 5:
        print(fb, "buzz")
    else:
        print(fb)	
    fb = fb + 1 
 
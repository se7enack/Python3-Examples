#!/usr/bin/env python3

fb=1

while fb <= 100:
    if 0 == fb % 3 + fb % 5:
        print("fizzbuzz")
    elif 0 == fb % 3:
        print("fizz")
    elif 0 == fb % 5:
        print("buzz")
    else:
        print(fb)	
    fb = fb + 1 
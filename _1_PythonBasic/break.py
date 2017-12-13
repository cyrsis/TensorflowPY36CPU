#!/usr/bin/env python
# -*- coding: utf-8 -*-


count = 0
while True:
    userInput = input("enter quit: ")
    # check for valid passwd
    if userInput == "quit" :
        break
    count = count + 1
    if count%3 > 0:
        continue
    print("Please input quit!")
    

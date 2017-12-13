#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    myList = [4, 6]
    print(myList[10])
    print("This is never been called")
except ZeroDivisionError as e:
    print("ZeroDivisionError happened")
    print(e)
except (IndexError, EOFError) as e:
    print("Exception happened")
    print(e)
else:
    print("No exception happened!")
finally:
    print("Process finished!")

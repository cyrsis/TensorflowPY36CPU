'''
Created on Aug 7, 2016
@author: Burkhard
'''




#======================
# imports
#======================
import tkinter as tk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

#======================
# functions
#======================
def get_current_windows_size():
    win.update()                        # to get runtime size
    print('width  =', win.winfo_width())
    print('height =', win.winfo_height())

def increase_window_width():
    # min width can not be resized to less
    # default heigth can be
    win.minsize(width=300, height=1)    # 1 = default

#======================
# Start GUI
#======================
get_current_windows_size()
increase_window_width()
print()
get_current_windows_size()

win.mainloop()


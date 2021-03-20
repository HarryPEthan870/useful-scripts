
#imports
import time, os
#coutdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    os.popen('killall yes')
    print("Time's up")
with open("num_interface.txt") as f:
    t = int(f.read())
countdown(t)

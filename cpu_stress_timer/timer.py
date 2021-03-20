
#imports
import time, os, sys
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
    write()
    print("Your temps are stored in temps.txt. You will find this file in the directory you ran this in.")
t = int(float(sys.argv[1]))
##file writing
def write():
    tw = str(t)
    f = open("temps.txt", "a")
    f.write("After ")
    f.write(tw)
    f.write(" seconds These are the temps")
    f.close()
    temps = os.popen('inxi -s >> temps.txt')
countdown(t)
# imports
import datetime as dt
import time, webbrowser, mouse
global TIME
# class
class infoClass:
    def __init__(self, cname, sclink, tlink, stime):
        self.cname = cname
        self.sclink = sclink
        self.tlink = tlink
        self.stime = stime
    def launch_all(self):
        webbrowser.open(self.sclink)
        webbrowser.open(self.tlink)
    def running(self):
        print(self.cname)
        print("has launched")
    def launched(self):
        print(self.cname)
        print("Had completed")

# information
MATH = infoClass("Math", "https://gateschili.schoology.com/course/2988867080", "https://teams.microsoft.com/l/meetup-join/19%3Ameeting_ZjUzZGQ0NjMtYTk1ZS00ZjRjLWFkYTItYTIyOWUzMjQ4MjI3%40thread.v2/0?context=%7B%22Tid%22%3A%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2C%22Oid%22%3A%22ee8a520f-ae60-4857-a361-6d30a6179ada%22%7D", "7:32")
ELA = infoClass("ELA", "https://gateschili.schoology.com/course/2988843027", "https://teams.microsoft.com/l/meetup-join/19%3A09835d9f2f7a4a899243ece210611498%40thread.tacv2/1599831942980?context=%7B%22Tid%22%3A%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2C%22Oid%22%3A%2272a88987-e123-4d69-a53b-6a3a23667df9%22%7D", "8:17")
BIO = infoClass("BIO", "https://gateschili.schoology.com/course/2988866856", "https://teams.microsoft.com/l/meetup-join/19%3aca2179956e7041aca03b909ae0c50d1e%40thread.tacv2/1620644993051?context=%7b%22Tid%22%3a%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2c%22Oid%22%3a%22b5647580-f1da-45fc-b65f-866c2fb97f00%22%7d", "8:57")
DDP = infoClass("DDP", "https://gateschili.schoology.com/course/2988930474", "https://teams.microsoft.com/l/meetup-join/19%3ameeting_YmExYWFkYTktODEzYi00NjRjLWFlM2YtODU0ZTY3Mzk2MjUy%40thread.v2/0?context=%7b%22Tid%22%3a%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2c%22Oid%22%3a%221c72287c-584b-4b89-bf2b-7cf13e3ad2dd%22%7d", "11:07")
Career = infoClass("Career", "https://gateschili.schoology.com/course/2988929821", "https://teams.microsoft.com/l/meetup-join/19%3a98e1f754eb28411c8f243516e62a2ec3%40thread.tacv2/1611862177068?context=%7b%22Tid%22%3a%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2c%22Oid%22%3a%22ba0e722e-f633-446c-86f8-e4db4069281e%22%7d", "11:52")
Global = infoClass("Global", "https://gateschili.schoology.com/course/2988886499", "https://teams.microsoft.com/l/meetup-join/19%3a52f3bde90117486da08bbffd5249500c%40thread.tacv2/1599941063269?context=%7b%22Tid%22%3a%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2c%22Oid%22%3a%22f9bdf3ba-632f-481d-b749-21702f4dc006%22%7d", "12:37")
Latin = infoClass("Latin", "https://gateschili.schoology.com/course/2988946475", "https://teams.microsoft.com/l/meetup-join/19%3afbe21b3407e4458f907caf80a1e5f419%40thread.tacv2/1600785073044?context=%7b%22Tid%22%3a%22e4c5ba9c-7fc0-4a21-8fa7-3e6a1d404866%22%2c%22Oid%22%3a%224654db56-5b23-49e2-ba80-995b6adbbdcf%22%7d", "1:22")
# mouse controls
def mouse():
    # leave meeting
    mouse.move(3210, 921, absolute=True, duration=0.2)
    mouse.click("left")
def mouse_2():
    # unmute
    mouse.move(2879, 633, absolute=True, duration=0.2)
    mouse.click("left")
    # join meeting
    mouse.move(2889, 581, absolute=True, duration=0.2)
    mouse.click("left")

# function
def run_stuff(name):
    name.running()
    mouse()
    name.launch_all()
    mouse_2()
    name.launched()
while True:
    TIME = dt.datetime.now().strftime("%H:%M")
    time.sleep(20)
    if TIME == MATH.stime:
        run_stuff(MATH)
    elif TIME == ELA.stime:
        run_stuff(ELA)
    elif TIME == BIO.stime:
        run_stuff(BIO)
    elif TIME == DDP.stime:
        run_stuff(DDP)
    elif TIME == Career.stime:
        run_stuff(Career)
    elif TIME == Global.stime:
        run_stuff(Global)
    elif TIME == Latin.stime:
        run_stuff(Latin)
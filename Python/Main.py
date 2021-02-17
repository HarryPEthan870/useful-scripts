#iports/global declaations
import subprocess, webbrowser
global classsel
#info for unser to chose
#coresponding numbers
print('Enter 1 for Math')
print('Enter 2 for ELA')
print('Enter 3 for Gym')
print('Enter 4 for Science')
print('Enter 5 for DDP')
print('Enter 6 for Career')
print('Enter 7 for Global')
print('Enter 8 for Latin')
#class selection
classsel = int(input("Enter Number coresponding to current class: "))
#var declration
if classsel == 1:
    classstr = "Math"
elif classsel == 2:
    classstr = "ELA"
elif classsel == 3:
    classstr = "Gym"
elif classsel == 4:
    classstr = "Science"
elif classsel == 5:
    classstr = "DDP"
elif classsel == 6:
    classstr = "Career"
elif classsel == 7:
    classstr = "Global"
elif classsel == 8:
    classstr = "Latin"
else:
    print('Please try again!')
    exit()
##input
print("You chose " + classstr)
boo_one = input('Is that correct(y/n) ')
#fail safe
if boo_one=="y":
    pass
else:
    print('Please try again!')
    exit()
#Teams
Teams = input("Is Teams open(y/n) ")
#urls
#Math
scmath = "https://gateschili.schoology.com/course/2988867080/materials"
#ELA
scela = "https://gateschili.schoology.com/course/2988843027/materials"
agendaela = "https://gateschilicsd-my.sharepoint.com/:w:/r/personal/noreynolds_gateschili_org/_layouts/15/guestaccess.aspx?e=KbbkTo&share=Ea792u-PRadCvwjaV33XIP0BKty5HkjyaUG1_JDIBNdSHg"
#Gym
scgym = "https://gateschili.schoology.com/course/2988901041/materials"
#Science
scscinece = "https://gateschili.schoology.com/course/2988866856/materials"
#DDP
scddp = "https://gateschili.schoology.com/course/2988930474/materials"
#Career
sccareer = "https://gateschili.schoology.com/course/2988929821/materials"
#Global
scglobal = "https://gateschili.schoology.com/course/2988886499/materials"
#Latin
sclatin = "https://gateschili.schoology.com/course/2988946475/materials"
onenote_latin = "https://gateschilicsd-my.sharepoint.com/:o:/r/personal/edlist_students_gateschili_org/_layouts/15/doc2.aspx?sourcedoc=%7Beadf0d79-79f3-4435-8920-6b03b915a4e4%7D&action=edit&wd=target%28Genral%20notes.one%7C8df6ea8f-830b-43c5-8f25-1979a8e50c5e%2FGender%20of%20nouns%7Cd7c562b3-37aa-4657-9adf-993d5f1160fb%2F%29"
#teams open
def Teams_run():
    if Teams=="n":
        subprocess.Popen('/home/harrypethan/.local/share/flatpak/app/com.microsoft.Teams/x86_64/stable/50d50c1a26163a110abf8dd0539b9f8e6642db09b0bc8abb25e8e221ab6d2571/export/bin/com.microsoft.Teams')
##functions
#Math
def Math():
    webbrowser.open(scmath, new=0)
    print("Remember to grab your Homework and Classwork packet!")
def ELA():
    webbrowser.open(scela, new=0)
    webbrowser.open(agendaela, new=0)
def Gym():
    webbrowser.open(scgym, new=0)
def Science():
    webbrowser.open(scscinece, new=0)
def DDP():
    webbrowser.open(scddp, new=0)
def Career():
    webbrowser.open(sccareer, new=0)
def Global():
    webbrowser.open(scglobal, new=0)
def Latin():
    webbrowser.open(sclatin, new=0)
    webbrowser.open(onenote_latin, new=0)
#web open
if classsel == 1:
    Math()
    Teams_run()
elif classsel == 2:
    ELA()
    Teams_run()
elif classsel == 3:
    Gym()
    Teams_run()
elif classsel == 4:
    Science()
    Teams_run()
elif classsel == 5:
    DDP()
    Teams_run()
elif classsel == 6:
    Career()
    Teams_run()
elif classsel == 7:
    Global()
    Teams_run()
elif classsel == 8:
    Latin()
    Teams_run()

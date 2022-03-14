from tkinter import *

'''main.py
* TODO
  + text file config
    +  each line: config = 2 then can remove whitespace and process
    + 
  + autoclicker
    + when click background, pause autoclicker
  + reload configs button
  + hold down things
    + implement with a checkbox menu (hold down w and left click or just w, etc)
  + global "something happening?" const that can be turned off by click background
'''
WORKING = False

AUTOCLICKING = False
AUTOCLICK_SPEED = 1000

screen = Tk()
screen.title('Automation GUI')

def stopAutomation():
    global WORKING
    WORKING = False

# set background image
img = PhotoImage(file="media\darkenedPurpleSky.png")
background = Label(screen, image=img)
background.bind("<Button-1>",lambda e: stopAutomation())
background.place(x=0, y=0, relwidth=1, relheight=1)

# main sidebar, put stuff in here
sidebar = Label()
sidebar.pack(side=LEFT)

def startAutoclick():
    global WORKING, AUTOCLICKING
    
    WORKING = True
    AUTOCLICKING = True
    autoclicker.after(0, autoclick())

def autoclick():
    global WORKING, AUTOCLICKING
    
    print("clicked once")

    if not WORKING:
        AUTOCLICKING = False
        
    if AUTOCLICKING:
        autoclicker.after(AUTOCLICK_SPEED, autoclick)

#
autoclicker = Label(sidebar, text="autoclick", font=("", 24), padx=20, pady=5, width=10)
autoclicker.bind("<Button-1>", lambda e: startAutoclick())
autoclicker.pack()

# 
holdLMB = Label(sidebar, text="hold LMB", font=("", 24), padx=20, pady=5, width=10)
holdLMB.bind("<Button-1>",lambda e: print("LMB clicked"))
holdLMB.pack()

# screen
screen.attributes('-fullscreen',True)
screen.bind("<Escape>", lambda e: screen.destroy())



screen.mainloop()

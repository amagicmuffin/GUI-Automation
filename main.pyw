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


### Autoclicking things
def autoclick():
    global WORKING, AUTOCLICKING
    
    print("clicked once")

    if not WORKING:
        AUTOCLICKING = False
        
    if AUTOCLICKING:
        autoclicker.after(AUTOCLICK_SPEED, autoclick)

autoclicker = Label(sidebar, text="autoclick", font=("", 24), padx=20, pady=5, width=10)
autoclicker.bind("<Button-1>", lambda e: startAutoclick())
autoclicker.pack()

### hold button things
holdLMB = Label(sidebar, text="hold LMB", font=("", 24), padx=20, pady=5, width=10)
holdLMB.bind("<Button-1>",lambda e: print("LMB clicked"))
holdLMB.pack()

### Toggle keyboard hold down
keyboardToggles = {
    "w": False,
    "a": False,
    "s": False,
    "d": False,
    "shift": False,
    "space": False
}

keyboardGUI = Label(sidebar)

def keyboardToggle(key):
    if keyboardToggles[key]:
        keyboardToggles[key] = False
    else:
        keyboardToggles[key] = True
holdWToggle = Label(keyboardGUI, text="W", font=("", 24), padx=5, pady=5)
holdWToggle.grid(row=0, column=1)
holdWToggle.bind("<Button-1>",lambda e: wToggle())

holdAToggle = Label(keyboardGUI, text="A", font=("", 24), padx=5, pady=5)
holdAToggle.grid(row=1, column=0)

holdSToggle = Label(keyboardGUI, text="S", font=("", 24), padx=5, pady=5)
holdSToggle.grid(row=1, column=1)

holdDToggle = Label(keyboardGUI, text="D", font=("", 24), padx=5, pady=5)
holdDToggle.grid(row=1, column=2)

holdShiftToggle = Label(keyboardGUI, text="Shift", font=("", 24), padx=5, pady=5)
holdShiftToggle.grid(row=2, column=0)

holdSpaceToggle = Label(keyboardGUI, text="Space", font=("", 24), padx=5, pady=5)
holdSpaceToggle.grid(row=2, column=1)

startHoldingBtn = Label(keyboardGUI, text="Start", font=("", 24), padx=5, pady=5)
startHoldingBtn.grid(row=2, column=2)

keyboardGUI.pack()

# screen
screen.attributes('-fullscreen',True)
screen.bind("<Escape>", lambda e: screen.destroy())



screen.mainloop()

from tkinter import *
import mouse
import keyboard

"""main.py
* TODO
  + text file config
    +  each line: config = 2 then can remove whitespace and process
    + use .ini, more research in phone
  + reload configs button
  + much later: refactor to not look terrible
"""
BACKGROUND_IMAGE = "darkBackground.png"

WORKING = False
BUFFER_TIME = 1000

AUTOCLICKING = False
AUTOCLICK_SPEED = 1000

screen = Tk()
screen.title("Automation GUI")


def stopAutomation():
    global WORKING
    WORKING = False


# set background image
img = PhotoImage(file=f"media//{BACKGROUND_IMAGE}")
background = Label(screen, image=img)
background.bind("<Button-1>", lambda e: stopAutomation())
background.place(x=0, y=0, relwidth=1, relheight=1)

# main sidebar, put stuff in here
sidebar = Label()
sidebar.pack(side=LEFT)


def startAutoclick():
    global WORKING, AUTOCLICKING

    WORKING = True
    AUTOCLICKING = True
    autoclicker.after(
        BUFFER_TIME, autoclick
    )  # immediately eval's autoclick()


# Autoclicking things
def autoclick():
    global WORKING, AUTOCLICKING

    print("clicked once")
    mouse.click()

    if not WORKING:
        AUTOCLICKING = False

    if AUTOCLICKING:
        autoclicker.after(AUTOCLICK_SPEED, autoclick)


autoclicker = Label(sidebar, text="autoclick", font=("", 24), padx=20, pady=5, width=10)
autoclicker.bind("<Button-1>", lambda e: startAutoclick())
autoclicker.pack()


# Toggle keyboard hold down
# shift is first so you dont fall off a cliff because crouch wasn't pressed
keyboardToggles = {
    "shift": False,
    "lmb": False,
    "rmb": False,
    "w": False,
    "a": False,
    "s": False,
    "d": False,
    "space": False,
}


def startHolding():
    for k, v in keyboardToggles.items():
        if k == "lmb" or k == "rmb" and v:
            mouse.hold(button="LEFT" if k == "lmb" else "RIGHT")
            continue
        if v:
            keyboard.press(v)


keyboardGUI = Label(sidebar)


def keyboardToggle(key, label):
    if keyboardToggles[key]:
        keyboardToggles[key] = False
        label.config(bg="grey94")  # default color
    else:
        keyboardToggles[key] = True
        label.config(bg="grey80")


# hold button things
holdLMBToggle = Label(keyboardGUI, text="LMB", font=("", 24), padx=20, pady=5)
holdLMBToggle.bind("<Button-1>", lambda e: keyboardToggle("lmb", holdLMBToggle))
holdLMBToggle.grid(row=0, column=0, sticky="nwes")

holdWToggle = Label(keyboardGUI, text="W", font=("", 24), padx=5, pady=5)
holdWToggle.grid(row=0, column=1, sticky="nwes")
holdWToggle.bind("<Button-1>", lambda e: keyboardToggle("w", holdWToggle))

holdRMBToggle = Label(keyboardGUI, text="RMB", font=("", 24), padx=20, pady=5)
holdRMBToggle.bind("<Button-1>", lambda e: keyboardToggle("rmb", holdRMBToggle))
holdRMBToggle.grid(row=0, column=2, sticky="nwes")

holdAToggle = Label(keyboardGUI, text="A", font=("", 24), padx=5, pady=5)
holdAToggle.grid(row=1, column=0, sticky="nwes")
holdAToggle.bind("<Button-1>", lambda e: keyboardToggle("a", holdAToggle))

holdSToggle = Label(keyboardGUI, text="S", font=("", 24), padx=5, pady=5)
holdSToggle.grid(row=1, column=1, sticky="nwes")
holdSToggle.bind("<Button-1>", lambda e: keyboardToggle("s", holdSToggle))

holdDToggle = Label(keyboardGUI, text="D", font=("", 24), padx=5, pady=5)
holdDToggle.grid(row=1, column=2, sticky="nwes")
holdDToggle.bind("<Button-1>", lambda e: keyboardToggle("d", holdDToggle))

holdShiftToggle = Label(keyboardGUI, text="Shift", font=("", 24), padx=5, pady=5)
holdShiftToggle.grid(row=2, column=0, sticky="nwes")
holdShiftToggle.bind("<Button-1>", lambda e: keyboardToggle("shift", holdShiftToggle))

holdSpaceToggle = Label(keyboardGUI, text="Space", font=("", 24), padx=5, pady=5)
holdSpaceToggle.grid(row=2, column=1, sticky="nwes")
holdSpaceToggle.bind("<Button-1>", lambda e: keyboardToggle("space", holdSpaceToggle))

startHoldingBtn = Label(keyboardGUI, text="Start", font=("", 24), padx=5, pady=5)
startHoldingBtn.grid(row=2, column=2, sticky="nwes")
startHoldingBtn.bind("<Button-1>", lambda e: startHoldingBtn.after(BUFFER_TIME, startHolding))

keyboardGUI.pack()

# screen
screen.bind("<Escape>", lambda e: screen.destroy())


screen.mainloop()

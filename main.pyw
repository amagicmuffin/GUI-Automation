from tkinter import *

'''main.py
* TODO
  + text file config
    +  each line: config = 2 then can remove whitespace and process
    + 
  + autoclicker
    + when click background, pause autoclicker
  + reload configs button
'''

screen = Tk()
screen.title('Automation GUI')

# set image
img = PhotoImage(file="media\darkenedPurpleSky.png")
background = Label(screen, image=img)
background.bind("<Button-1>",lambda e: print("background clicked"))
background.place(x=0, y=0, relwidth=1, relheight=1)

# main sidebar, put stuff in here
sidebar = Label()
sidebar.pack(side=LEFT)

# 
autoclicker = Label(sidebar, text="autoclick", font=("", 24), padx=20, pady=5, width=10)
autoclicker.bind("<Button-1>",lambda e: print("autoclicker clicked"))
autoclicker.pack()

# 
holdLMB = Label(sidebar, text="hold LMB", font=("", 24), padx=20, pady=5, width=10)
holdLMB.bind("<Button-1>",lambda e: print("LMB clicked"))
holdLMB.pack()

# screen
screen.attributes('-fullscreen',True)
screen.bind("<Escape>", lambda e: screen.destroy())



screen.mainloop()

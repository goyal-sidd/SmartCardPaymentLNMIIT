from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

def pad1():
   TkMessageBox.showinfo( "Number 1")
   #server code for 1

def pad2():
   TkMessageBox.showinfo( "Number 2")
   #server code for 1
   
def pad3():
   TkMessageBox.showinfo( "Number 3")
   #server code for 1

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="1", command = pad1)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="2")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="3")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="4")
blackbutton.pack( side = LEFT)

blackbutton = Button(bottomframe, text="5")
blackbutton.pack( side = LEFT)

blackbutton = Button(bottomframe, text="6")
blackbutton.pack( side = LEFT)

root.mainloop()

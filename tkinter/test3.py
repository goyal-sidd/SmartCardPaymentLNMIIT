import Tkinter
import tkMessageBox

top = Tkinter.Tk()

frame = Tkinter.Frame(top)
frame.pack()

bottomframe = Tkinter.Frame(top)
bottomframe.pack( side = BOTTOM )

def pad1():
   tkMessageBox.showinfo( "Number 1")
   #server code for 1

def pad2():
   tkMessageBox.showinfo( "Number 2")
   #server code for 1
   
def pad3():
   tkMessageBox.showinfo( "Number 3")
   #server code for 1
   

A = Tkinter.Button(top, text ="1", command = pad1)

B = Tkinter.Button(top, text ="2", command = pad2)

C = Tkinter.Button(top, text ="3", command = pad3)

A.pack(side = LEFT)
B.pack(side = LEFT)
C.pack(side = LEFT)
top.mainloop()

from Tkinter import *

# ---------- VARIABLES & UNBIND ----------
def get_data(event):
 
    # Output the values for the Widgets with get()
    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Boolean :", boolVar.get())
 
# You can unbind and rebind an event to a function
def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)
def FocusLogin(self,event):
    os.system('florence')
root = Tk()
root.geometry("700x400+300+300")

# As I showed previously there are TkInter variables
# you can use with Widgets to set and get values
strVar = StringVar()
intVar = IntVar()
boolVar = BooleanVar()
 
# Set the default values with set()
intVar.set("Enter Amount")
strVar.set("Remarks")
boolVar.set(False)
 
# Assign the variable to either textvariable or variable
strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)
 
intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)
 
 
# Depending on if this check button is selected or not
# will determine if we can get data on our Widgets
theCheckBut = Checkbutton(root, text="Are You Sure for this payment", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)
 
# Call the function get_data on click
getDataButton = Button(root, text="PAY")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)
 
root.mainloop()

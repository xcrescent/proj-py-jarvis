import tkinter.messagebox
from tkinter import *

#https://pythongeeks.org/gui-programming-in-python/#:~:text=%20GUI%20Programming%20in%20Python%20%201%20Python,color%20and%20a%20circle%20of%20red...%20More%20


win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
win.geometry('1000x800') #setting the size of the window

def func():#function of the button
    tkinter.messagebox.showinfo("Greetings","Hello! Welcome to PythonGeeks.")

#Button
btn=Button(win,text="Click Me", width=10,height=2,command=func)
btn.place(x=300,y=120)

#Canvas
# can=Canvas(win, width=100, height=100) #creating the canvas
# oval=can.create_oval(75, 50, 75, 50,fill='green') #drawing an oval 
# can.pack()

#check button
cb_var1 = IntVar() 
cb1=Checkbutton(win, text='Python', variable=cb_var1,onvalue=1,offvalue=0,height=5,width=20).grid(row=3, sticky=W) 
cb_var2 = IntVar() 
cb2=Checkbutton(win, text='C++', variable=cb_var2,onvalue=1,offvalue=0,height=5,width=20).grid(row=4, sticky=W) 
cb_var3 = IntVar() 
cb3=Checkbutton(win, text='Java', variable=cb_var3,onvalue=1,offvalue=0,height=5,width=20).grid(row=5, sticky=W) 

#entry
Label(win, text='Name').grid(row=0) 
Label(win, text='Email').grid(row=1) 
ent1 = Entry(win) 
ent2 = Entry(win) 
ent1.grid(row=0, column=1) 
ent2.grid(row=1, column=1) 


win.mainloop() #running the loop that works as a trigger
#Riley
#Comp Prog
#10/15/18

import tkinter
from tkinter import ttk
from tkinter import *

root=Tk()
combovar=StringVar()
spinvar=StringVar()
resultsContents=StringVar()
all_comboboxes=[]

def about(): #Makes a new box.
    EX=Toplevel(root)
    aboL=Label(EX, text='''This program was made by Riley
Underwood as a project for his school.

The purpose of this program in to
write to a file the choices about
where and how the user traveled.

This Project was started on 10/15/18
and was completed... UNKOWN.''') #Creates a label that says what's in the ".
    aboL.grid(column=1, row=1, sticky="NSEW")
    EX.grid_columnconfigure(1,weight=1)
    EX.grid_rowconfigure(1,weight=1)

def clear(): #Clears all enetered data.
   combovar.set("V-Type of Travel-V")
   spinvar.set("V-Month-V")
   resultsContents.get=""
   notT.delete("1.0", END)
   couLB.selection_clear(0, END)

def QUIT(): #Quits.
   quit()

def submit(*args): #Adds 34 percent to progressbar if hassent already, adds up price and displays it.
##    if spinvar.get() == 1:
##        spinvar.set("January")
##    elif spinvar.get() == 2:
##        spinvar.set("Febuary")
##    elif spinvar.get() == 3:
##        spinvar.set("March")
##    elif spinvar.get() == 4:
##        spinvar.set("April")
##    elif spinvar.get() == 5:
##        spinvar.set("May")
##    elif spinvar.get() == 6:
##        spinvar.set("June")
##    elif spinvar.get() == 7:
##        spinvar.set("July")
##    elif spinvar.get() == 8:
##        spinvar.set("August")
##    elif spinvar.get() == 9:
##        spinvar.set("September")
##    elif spinvar.get() == 10:
##        spinvar.set("October")
##    elif spinvar.get() == 11:
##        spinvar.set("November")
##    elif spinvar.get() == 12:
##        spinvar.set("December")
##    else:
##        print ("Please choose an option!")
##        clear()
    ledcheck=open("trip_ledge.txt", "a")
    ledcheck.write("Country: " +str(couLB.get("2"))+ ", Month: " +str(spinvar.get())+ ", Mode of Travel: " +str(combovar.get())+ ", Notes: " +str(notT.get(1.0, END))) #Shows all applied data.
    ledcheck.write("\n====================================================================================\n")  #For organising.
    ledcheck.close()

########################### Widgets ###########################

menubar=Menu(root)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=submit)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=QUIT)
menubar.add_cascade(label="File", menu=filemenu) #Create a pulldown menu, and add it to the menu bar.

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu) #Makes a help dropdown menu.

namL=Label(root, text="My trip to another country:") #Creates a label that says what's in the ".
namL.grid(column=10, row=10, sticky="NSEW")

ch1CB=ttk.Combobox(root, state="readonly", textvariable=combovar, values=("Air", "Train", "Car")) #Creates a combo box that can't be manually typed in with the given values.
ch1CB.set("V-Type of Travel-V") #Makes a starting value.
ch1CB.grid(column=20, row=30, columnspan=30, sticky="NSEW")
all_comboboxes.append(ch1CB) #Adds to list of comboboxes.

couL=Label(root, text="Countries:") #Creates a label that says what's in the ".
couL.grid(column=10, row=19, sticky="NSEW")
couLB=Listbox(root) #A listbox of some countries.
couLB.grid(column=10, row=20, sticky="NSEW")
couLB_list=["America", "Australia", "Canada", "Germany", "Greece", "Italy", "India", "Iraq", "Jamaica", "Mexico", "Mongolia", "Romania", "Russia", "Thailand", "Turkey"]
for x in couLB_list:
   couLB.insert(END, x)
couSB = ttk.Scrollbar(root, orient=VERTICAL, command=couLB.yview)
couSB.grid(column=11, row=20, sticky="NSEW")
couLB['yscrollcommand']=couSB.set

notL=Label(root, text="Notes:") #Creates a label that says what's in the ".
notL.grid(column=20, row=19, sticky="NSEW")
notT=Text(root, width=5, height=5)
notT.grid(column=20, row=20, columnspan=30, sticky="NSEW")

SB_list=["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
SB=Spinbox(root, values=SB_list, textvariable=spinvar)
SB.grid(column=10, row=30, sticky="NSEW")
spinvar.set("V-Month-V")

canB=ttk.Button(root, text="Clear", command=clear)  #Creates a "Cancel" button.
canB.grid(column=10, row=40, sticky="NSEW")
subB=ttk.Button(root, text="Submit", command=submit)  #Creates a "Submit" button.
subB.grid(column=20, row=40, columnspan=30, sticky="NSEW")

ttk.Sizegrip().grid(column=999, row=999, sticky=(S,E))

########################Grid#############################

root.grid_columnconfigure(10,weight=1)
root.grid_columnconfigure(20,weight=1)
root.grid_columnconfigure(30,weight=1)
root.grid_rowconfigure(10,weight=1)
root.grid_rowconfigure(19,weight=1)
root.grid_rowconfigure(20,weight=1)
root.grid_rowconfigure(30,weight=1)
root.grid_rowconfigure(40,weight=1)

root.title("@Trippy Bruh@") #Makes the title what is in the "s.
root.config(menu=menubar) #Display the menu.
root.mainloop()
root.destroy()

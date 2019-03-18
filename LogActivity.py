from tkinter import *

class LogActivity:
    def __init__(self,master):
        self.master = master
        master.title("Log Activity")
        label = Label(master, text="Log Here: ")
        workitem = Label(master, text="defib_patient1")
        doctor = Label(master, text="John")
        self.log = StringVar()
        log = Entry(master, textvariable=self.log)
        button = Button(master, text="LOG", command=lambda: self.gotoNextActivity())

        doctor.grid(row=0,column=7)
        workitem.grid(row=0,column =0)
        label.grid(row=1,column=0)
        log.grid(row=1,column=7)
        button.grid(row=2,column=0,columnspan=10,sticky=W+E)

    def gotoNextActivity(self):
        return

root = Tk()
my_gui = LogActivity(root)
root.mainloop()



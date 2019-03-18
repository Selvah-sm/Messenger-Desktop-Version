from tkinter import *

class WorkItemActivity:

    def __init__(self,master):

        self.master = master
        master.title("Work Item")
        teamcode = "102"
        if teamcode == "101":
            workitemlist = ["defib_patient1","defib_patient2"]
        elif teamcode == "102":
            workitemlist = ["defib_patient3", "defib_patient4"]

        for x in workitemlist:
            button = Button(master,text = x, command=lambda: self.gotoNextActivity())
            button.pack()
    def gotoNextActivity(self):
        return

root = Tk()
my_gui = WorkItemActivity(root)
root.mainloop()

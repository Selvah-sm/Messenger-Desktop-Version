from tkinter import *

class TeamJoin:

    def __init__(self,master):
        self.master = master
        master.title("Register Device")
        label = Label(master, text="Team Code: ")
        label.pack()
        self.teamid = StringVar()
        TeamID = Entry(master, textvariable=self.teamid)
        TeamID.pack()
        btnJoin = Button(master, text="Join Team", command=lambda: self.gotoNextActivity())
        btnJoin.pack()

    def gotoNextActivity(self):
        return

root = Tk()
my_gui = TeamJoin(root)
root.mainloop()
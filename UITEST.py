from tkinter import *
from uuid import getnode as get_mac
from Server  import *
import requests

URL = "http://ec2-35-171-185-240.compute-1.amazonaws.com"
class Frames(object):


    def __init__(self):
        pass

    def main_frame(self, root):
        root.title('REGISTER')
        #root.geometry('1600x150')
        self.query = StringVar()
        Label(root, text="UUID: "+str(get_mac())).pack(padx=10, pady=50)
        Label(root, text='Enter Nick Name').pack(padx=10, pady=50)
        Entry(root, textvariable=self.query).pack(padx=10, pady=50)
        Button(root, text="Register", command=self.team_frame).pack()

    def team_frame(self):
        print(self.query.get())
        global URL
        print(URL)
        PARAMS = {'username':str(self.query.get()),'text':str(get_mac())}
        r= requests.post(url=URL+"/registration",data=PARAMS)
        print(r)
        result = Toplevel()
        result.title('TEAM')
        result.attributes('-fullscreen', True)
        result.bind('<Escape>',lambda e: result.destroy())
        self.teamName = StringVar()
        Label(result, text="Welcome: "+self.query.get()).pack(padx=10, pady=30)
        Label(result, text="Enter Team Code: ").pack(padx=10, pady=30)
        Entry(result, textvariable=self.teamName).pack(padx=10, pady=30)
        Button(result, text="JOIN", command=self.workitem_frame).pack(padx=10, pady=30)

    def workitem_frame(self):
        global URL
        PARAMS = {'text': str(self.teamName.get()), 'uid': str(get_mac())}
        r = requests.post(url=URL + "/jointeam", data=PARAMS)
        print(r)
        result = Toplevel()
        result.title(self.teamName.get()+' - WORK ITEM')
        result.attributes('-fullscreen', True)
        result.bind('<Escape>',lambda e: result.destroy())
        print(self.teamName.get())
        Label(result, text="TEAM JOINED: "+self.teamName.get()).pack(padx=10, pady=50)
        self.selectedItem = StringVar()
        workitemlist = []
        if  self.teamName.get()== "101":
            print('inside if')
            workitemlist.append("defib_patient1")
            workitemlist.append("defib_patient2")
        elif self.teamName.get() == "102":
            workitemlist.append("defib_patient3")
            workitemlist.append("defib_patient4")

        for x in workitemlist:
            Button(result, text=x, command=lambda x=x:self.logging_frame(x)).pack(padx=10, pady=10)
    def logging_frame(self, clickedButton):
        result = Toplevel()
        result.title(clickedButton+' - Log Frame')
        result.attributes('-fullscreen', True)
        result.bind('<Escape>', lambda e: result.destroy())
        Label(result, text="DOCTOR: "+self.query.get()).pack()
        Label(result, text="WORKITEM: "+clickedButton).pack()

        Button(result, text="Charge", command=lambda: self.logHere()).pack(padx=10, pady=10)
        Button(result, text="Discharge", command=lambda: self.logHere()).pack(padx=10, pady=10)
        Button(result, text="100 Joules", command=lambda: self.logHere()).pack(padx=10, pady=10)
        Button(result, text="200 Joules", command=lambda: self.logHere()).pack(padx=10, pady=10)
        Button(result, text="300 Joules", command=lambda: self.logHere()).pack(padx=10, pady=10)
        Button(result, text="400 Joules", command=lambda: self.logHere()).pack(padx=10, pady=10)

        listbox = Listbox(result)
        listbox.pack()

        listbox.insert(END, "a list entry")

        for item in ["one", "two", "three", "four"]:
            listbox.insert(END, item)

    def logHere(self):
        return

root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
app = Frames()
app.main_frame(root)
root.mainloop()


import tkinter as tk

class RegistrationActivity(tk.Frame):
    Username = ""
    UUID = ""

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        #master.title("Register Device")
        label = tk.Label(master,text = "User Name: ")
        label.pack()
        self.uname = tk.StringVar()
        UserName = tk.Entry(master,textvariable=self.uname)
        UserName.pack()


        btnRegister = tk.Button(master, text="Register", command=lambda :  controller.show_frame())
        btnRegister.pack()




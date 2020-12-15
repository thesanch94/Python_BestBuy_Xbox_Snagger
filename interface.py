import os
from datetime import datetime
from tkinter import *
from pytz import timezone
import xbox_snagger


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.projectdirectory = os.getcwd()
        self.master = master
        self.initwindow = self.init_window()
        self.bot = None

    def client_exit(self):
        exit()


    def callprint(self, message, tzone='US/Central'):
        tzone = timezone(tzone)
        sMessage = message
        now = datetime.now(tzone)
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


    def init_window(self):

        self.master.title("XBOX Snagger")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        self.text_email = Label(self, text="Best Buy Email")
        self.text_email.place(x=150, y=45)
        self.entry_email = Entry(self.master)
        self.entry_email.place(x=275, y=45)

        self.text_password = Label(self, text="Best Buy Password")
        self.text_password.place(x=150, y=80)
        self.entry_pw = Entry(self.master, show="*")
        self.entry_pw.place(x=275, y=80)

        button = Button(self, text="Initialize Chromedriver", command=self.initialize)
        button.place(x=5, y=5)

        button = Button(self, text="Login to Bestbuy", command=self.login)
        button.place(x=5, y=40)

        button = Button(self, text="Begin the Snagging", command=self.loop_until_snag)
        button.place(x=5, y=75)

    def initialize(self):
        un = str(self.entry_email.get())
        pw = str(self.entry_pw.get())
        if un == "" or pw == "":
            self.callprint("Please specify a valid email and password")
            return
        self.bot = xbox_snagger.xbox_snagger(un, pw, os.getcwd())
        self.bot.initiate_driver()

    def login(self):
        self.bot.login_bestbuy()

    def loop_until_snag(self):
        self.bot.loop_wait_and_add_to_cart()





root = Tk()
root.geometry("600x500")
app = Window(root)
root.mainloop()
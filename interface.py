import os
from datetime import datetime
from tkinter import *
from pytz import timezone
import chrome_bot
import sys

class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.projectdirectory = os.getcwd()
        self.master = master
        self.initwindow = self.init_window()
        self.bot = None

    def client_exit(self):
        sys.exit()


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

        button = Button(self, text="Initialize Chromedriver", command=self.initialize)
        button.place(x=5, y=5)

        self.text_email = Label(self, text="Be sure to manually login after initializing the chrome driver!")
        self.text_email.place(x=145, y=5)

        button = Button(self, text="Begin the Snagging", command=self.loop_until_snag)
        button.place(x=5, y=40)

        self.text_email = Label(self, text="Product URL, Defaulted to Xbox Series X, must be a BEST BUY online product")
        self.text_email.place(x=5, y=75)
        self.entry_productURL = Entry(self.master, width=75)
        self.entry_productURL.insert(END, "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324")
        self.entry_productURL.place(x=5, y=110)

    def initialize(self):

        self.bot = chrome_bot.chrome_bot(os.getcwd())
        self.bot.initiate_driver()

    def login(self):
        self.bot.login_bestbuy()

    def loop_until_snag(self):
        url = str(self.entry_productURL.get())
        self.bot.loop_wait_and_add_to_cart(url)





root = Tk()
root.geometry("600x200")
app = Window(root)
root.mainloop()
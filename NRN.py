import tkinter as tk

LARGE_FONT = ("Arial", 12)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}

        frame = StartPage(container, self)

        self.frame[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()



    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Quit', command=self.quit)
        self.quitButton.grid()

        self.userNameDialog = tk.Entry(master=None)
        self.userNameDialog.grid()

        self.passwordDialog = tk.Entry(master=None, show="*")
        self.passwordDialog.grid()

        self.serverDialog = tk.Entry(master=None)
        self.serverDialog.grid()

        self.testButton = tk.Button(self, text='Create Connection', command=lambda *args: self.assignVariables())
        self.testButton.grid()


    def assignVariables(self):
        username = self.userNameDialog.get()
        password = self.passwordDialog.get()
        servername = self.serverDialog.get()

        self.userNameDialog.delete(0, 'end')
        self.passwordDialog.delete(0,'end')
        self.serverDialog.delete(0,'end')
        try:
            from plexapi.myplex import MyPlexAccount
            account = MyPlexAccount(username, password)
            plex = account.resource(servername).connect()
            self.plexStatus = tk.Label(master=None, text="Plex Connection Successful")
            self.plexStatus.grid()
            self.plexFrame()

        except BaseException:
            self.plexStatusFail = tk.Label(master=None, text="Plex Connection Unsuccessful. Please try again.")
            self.plexStatusFail.grid()
    def plexFrame(self):
        window = tk.Toplevel(self)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        userNameEntry = tk.Entry()
        userNameEntry.pack()
        passwordEntry = tk.Entry(show="*")
        passwordEntry.pack()
        serverEntry = tk.Entry()
        serverEntry.pack()

        def assignVar():
            username = userNameEntry.get()
            password = passwordEntry.get()
            servername = serverEntry.get()

            userNameEntry.delete(0, 'end')
            passwordEntry.delete(0, 'end')
            serverEntry.delete(0, 'end')
            try:
                from plexapi.myplex import MyPlexAccount
                account = MyPlexAccount(username, password)
                plex = account.resource(servername).connect()
                plexStatus = tk.Label(master=None, text="Plex Connection Successful")
                plexStatus.pack()

            except BaseException:
                plexStatusFail = tk.Label(master=None, text="Plex Connection Unsuccessful. Please try again.")
                plexStatusFail.pack()

        button1 = tk.Button(self, text="Connect to Server", command=lambda: assignVar())
        button1.pack()

app = Application()
app.mainloop()


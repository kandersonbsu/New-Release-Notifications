import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

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
        except BaseException:
            self.plexStatusFail = tk.Label(master=None, text="Plex Connection Unsuccessful. Please try again.")
            self.plexStatusFail.grid()


app = Application()
app.master.title('Plex Stats')
app.mainloop()

library = plex.library.section('Movies')
print(library.recentlyAdded(3))

import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Quit', command=self.quit)
        self.quitButton.grid()



app = Application()
app.master.title('Plex Stats')
app.mainloop()


userName = input("User Name: ")
password = input("Password: ")
serverName = input("Server Name: ")

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(userName, password)
plex = account.resource(serverName).connect()

library = plex.library.section('Movies')
print(library.recentlyAdded(3))

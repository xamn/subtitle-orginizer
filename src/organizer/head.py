from subtitleOrganizer import subtitleOrganizer 
from tkinter import *


#currently only windows compatible
subRepository = 't:\\subtitles\\'
movieShack = 't:\\Movieshack\\'


class theGui(Frame):

    def createWidgets(self):
        self.subLabel = Label(self, text="Subtitle Location:")
        self.subLabel.pack({"side": "top", "padx": 10})
        
        self.subBox = Entry(self)
        self.subBox.insert(INSERT,subRepository)
        self.subBox.pack({"side": "top"})
        
        self.tvLabel = Label(self, text="Tv Location:")
        self.tvLabel.pack({"side": "top", "padx": 10})
        
        self.tvBox = Entry(self)
        self.tvBox.insert(INSERT,movieShack)
        self.tvBox.pack({"side": "top"})
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "bottom"})
        self.organize = Button(self)
        self.organize["text"] = "ORGANIZE"
        self.organize["command"] = self.organize
        self.organize.pack({"side": "bottom"})
        
        


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.organizer = None
        
    def organize(self):
        if not self.organizer:
            self.organizer = subtitleOrganizer(self.subBox.get(),self.tvBox.get())
        self.organizer.organize()
        
        
        

root = Tk()
app = theGui(master=root)
app.mainloop()
root.destroy()
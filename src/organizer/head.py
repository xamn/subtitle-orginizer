from subtitleOrganizer import subtitleOrganizer 
from tkinter import *





class theGui(Frame):
    
    def organizeRepository(self):
        
        if not self.organizer \
           or self.subRepository != self.subBox.get() \
           or self.movieShack != self.tvBox.get():
            self.subRepository = self.subBox.get()
            self.movieShack = self.tvBox.get()
            self.organizer = subtitleOrganizer(self.subRepository,self.movieShack)
        
        self.organizer.organize()

    def createWidgets(self):
        self.subLabel = Label(self, text="Subtitle Location:")
        self.subLabel.grid(row=0,column=0)
        
        self.subBox = Entry(self)
        self.subBox.insert(INSERT,self.subRepository)
        self.subBox.grid(row=0,column=1)
        
        self.tvLabel = Label(self, text="Tv Location:")
        self.tvLabel.grid(row=1,column=0)
        
        self.tvBox = Entry(self)
        self.tvBox.insert(INSERT,self.movieShack)
        self.tvBox.grid(row=1,column=1)
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=2,column=1)
        
        self.organize = Button(self)
        self.organize["text"] = "ORGANIZE"
        self.organize["command"] = self.organizeRepository
        self.organize.grid(row=2,column=0)
        
        


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        #defaults
        self.subRepository = '/Users/xamn/pythonplay/SubRep/'
        self.movieShack = '/Users/xamn/pythonplay/Movieshack/'
        self.createWidgets()
        self.organizer = None
        
        
        
    
        
        
        

root = Tk()
app = theGui(master=root)
app.mainloop()
root.destroy()
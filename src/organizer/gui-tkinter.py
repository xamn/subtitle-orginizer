from subtitleOrganizer import subtitleOrganizer 
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import Directory




class theGui(Frame):
    
    def organizeRepository(self):
        
        #remove, even though repository exists contents may have changed
        #if not self.organizer \
        #   or self.subRepository != self.subBox.get() \
        #   or self.movieShack != self.tvBox.get():
            self.subRepository = self.subBox.get()
            self.movieShack = self.tvBox.get()
            try:
                self.organizer = subtitleOrganizer(self.subRepository,self.movieShack)
            except OSError as detail:
                showerror("Organize Error", detail)
            else:
                self.organizer.organize()
    
    def organizeRecRepository(self):
        self.subRepository = self.subBox.get()
        self.movieShack = self.tvBox.get()
        try:
            self.organizer = subtitleOrganizer(self.movieShack,self.movieShack)
        except OSError as detail:
            showerror("Organize Error", detail)
        else:
            self.organizer.organizeRep()

    def createWidgets(self):
        self.subLabel = Label(self, text="Subtitle Location:")
        self.subLabel.grid(row=0,column=0)
        
        self.subBox = Entry(self)
        self.subBox.insert(INSERT,self.subRepository)
        self.subBox.grid(row=0,column=1)
        
        self.browseSub = Button(self)
        self.browseSub["text"] = "Browse"
        self.browseSub["command"] = self.subBrowse
        self.browseSub.grid(row=0,column=3)
        
        self.tvLabel = Label(self, text="Tv Location:")
        self.tvLabel.grid(row=1,column=0)
        
        self.tvBox = Entry(self)
        self.tvBox.insert(INSERT,self.movieShack)
        self.tvBox.grid(row=1,column=1)
        
        self.browsetv = Button(self)
        self.browsetv["text"] = "Browse"
        self.browsetv["command"] = self.tvBrowse
        self.browsetv.grid(row=1,column=3)
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=2,column=2)
        
        self.organize = Button(self)
        self.organize["text"] = "ORGANIZE"
        self.organize["command"] = self.organizeRepository
        self.organize.grid(row=2,column=0)
        
        self.organize2 = Button(self)
        self.organize2["text"] = "ORGANIZE REP"
        self.organize2["command"] = self.organizeRecRepository
        self.organize2.grid(row=2,column=1)
        
    
    def tvBrowse(self):
        self.showbox(self.tvBox,self.movieShack)
    
    def subBrowse(self):
        self.showbox(self.subBox,self.subRepository)
        
    def showbox(self,tWidget,tvar):
        #messagebox.showwarning("Open file", "Cannot open this file\n")
        #showerror("Open file", "Cannot open this file\n")
        z = Directory()
        tvar = z.show()
        tWidget.delete(0,END)
        tWidget.insert(INSERT,tvar)
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0,column=0)
        #defaults
        self.subRepository = '/Users/xamn/pythonplay/SubRep/'
        self.movieShack = '/Users/xamn/pythonplay/Movieshack/'
        self.createWidgets()
        self.organizer = None
        
        

        

root = Tk()
app = theGui(master=root)
app.mainloop()
root.destroy()
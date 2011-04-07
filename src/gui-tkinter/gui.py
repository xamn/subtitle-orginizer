from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.subLabel = Label(self, text="Subtitle Location:")
        self.subLabel.pack({"side": "top", "padx": 10})
        
        self.subBox = Entry(self)
        self.subBox.insert(INSERT,"test Box")
        self.subBox.pack({"side": "top"})
        
        self.tvLabel = Label(self, text="Tv Location:")
        self.tvLabel.pack({"side": "top", "padx": 10})
        
        self.tvBox = Entry(self)
        self.tvBox.insert(INSERT,"test Box 2")
        self.tvBox.pack({"side": "top"})
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "bottom", "padx": 100})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
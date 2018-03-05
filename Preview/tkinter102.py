from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button1 = Button(self, text='Press', command=self.reply)
        #button2 = Button(self, text='Press too', command=self.reply)
        button1.pack()
        #button2.pack()

    def reply(self):
        showinfo(title='popup', message='Button Pressed!')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()

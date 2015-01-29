__author__ = 'root'

from Tkinter import *

class InvForm:
    def __init__(self):

        # initialize the form
        self.root = Tk()
        self.root.title("Inventory Application Form")
        add = Radiobutton(self.root, text = "add server", value = '12').grid(row=0, column = 0)
        edit = Radiobutton(self.root, text = "edit server", value = '14').grid(row=0, column = 1)

        LnumHDD = Label(self.root, text = "Number of HDDs:").grid(row=1,column=0)
        EnumHDD = Entry(self.root).grid(row=1, column = 1)
        LsizeHDD = Label(self.root, text = "Size of HDDs:").grid(row=2,column=0)
        EsizeHDD = Entry(self.root).grid(row=2, column = 1)
        Lmem = Label(self.root, text = "Memory:").grid(row=3,column=0)
        Emem = Entry(self.root).grid(row=3, column = 1)
        LnumProc = Label(self.root, text = "Processors:").grid(row=4,column=0)
        EnumProc = Entry(self.root).grid(row=4, column = 1)
        closeButton = Button(self.root, text = "Exit", command = self.close).grid(row=6, column = 0)
        self.var = StringVar(self.root)
        self.var.set('Server Name')
        self.choices = ['R610','R710','R720','R620','R630','R730XD']
        self.option = OptionMenu(self.root,self.var,*self.choices)
        self.option.grid(row=0,column=2)
        self.button = Button(self.root,text="Apply",command=self.systemType)
        self.button.grid(row=6,column=1)
        self.root.mainloop()

    def close(self):
        print "Thank you for using the Inventory Application Form"
        self.root.destroy()
    def systemType(self):
        sf = "value is %s" % self.var.get()
        self.root.title(sf)
        color = self.var.get()
        self.root['bg'] = color

if __name__ == "__main__":
    print "please launch using blah blah"
    form = InvForm()
    form()
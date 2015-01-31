__author__ = 'root'
from Tkinter import *
from modules.valid_IP import *
# from anydbm import *
class InvForm:
    def __init__(self):
        # initialize the form
        self.root = Tk()
        self.root.title("Inventory Application Form")
        #add/edit radio buttons
        self.add = Radiobutton(self.root,indicatoron=False,state=NORMAL,text = "add server",width=16,value = '1',variable=1)
        self.add.grid(row=0, column = 0)
        self.edit = Radiobutton(self.root,indicatoron=False,text = "edit server",width=16,value = '2',variable=1)
        self.edit.grid(row=0, column = 1)
        self.add.select()
        #entry labels/entries
        self.numHDDlabel = Label(self.root, text = "Number of HDDs:").grid(row=1,column=0)
        self.numHDDentry = Entry(self.root)
        self.numHDDentry.grid(row=1, column = 1)
        self.sizeHDDlabel = Label(self.root, text = "Size of HDDs:").grid(row=2,column=0)
        self.sizeHDDentry = Entry(self.root)
        self.sizeHDDentry.grid(row=2, column = 1)
        self.memLabel = Label(self.root, text = "Memory:").grid(row=3,column=0)
        self.memEntry = Entry(self.root)
        self.memEntry.grid(row=3, column = 1)
        self.numProcLabel = Label(self.root, text = "Processors:").grid(row=4,column=0)
        self.numProcEntry = Entry(self.root)
        self.numProcEntry.grid(row=4, column = 1)
        self.IPdracLabel = Label(self.root,text = "DRAC IP address:").grid(row=5,column=0)
        self.IPdracEntry = Entry(self.root)
        self.IPdracEntry.grid(row=5,column=1)
        self.ip1Label = Label(self.root,text = "IP address 1:").grid(row=6,column=0)
        self.ip1Entry = Entry(self.root)
        self.ip1Entry.grid(row=6,column=1)
        self.ip2Label = Label(self.root,text = "IP address 2:").grid(row=7,column=0)
        self.ip2Entry = Entry(self.root)
        self.ip2Entry.grid(row=7,column=1)
        self.serviceTagLabel = Label(self.root,text="Service Tag:").grid(row=8,column=0)
        self.serviceTagEntry = Entry(self.root)
        self.serviceTagEntry.grid(row=8,column=1)
        #description
        self.descriptionLabel = Label(self.root,text="Description:").grid(row=1,column=2)
        self.descriptionEntry = Entry(self.root)
        self.descriptionEntry.grid(row=2,column=2,rowspan=7,sticky=N+S)
        self.descriptionEntry.insert(0,"needs formatting/wordwrap")
        #bottom buttons
        self.closeButton = Button(self.root, text = "Exit", command=self.closeFunc,width=16).grid(row=10, column = 2)
        self.applyButton = Button(self.root,text="Apply",command=self.applyFunc,width=16).grid(row=10,column=1)
        self.clearButton = Button(self.root,text="Clear",command=self.clearFunc,width=16).grid(row=10,column=0)
        #drop down list
        self.var = StringVar(self.root)
        self.var.set('Server Model')
        serverModels = ['R610','R710','R720','R620','R630','R730XD']
        self.choices = serverModels
        # I think you can put all 3 lines on one line, more readable (JN)
        self.option = OptionMenu(self.root,self.var,*self.choices).grid(row=0, column=2, columnspan=2)
        # self.option.config(width=13)
        # self.option.grid(row=0,column=2)

        self.root.mainloop()
    def closeFunc(self):
        print "Thank you for using the Inventory Application Form"
        self.root.destroy()
    def applyFunc(self):
        newTitle = "Server is %s." % self.var.get()
        self.writeNumHDDentry()
        self.writeSizeHDDentry()
        self.writeMemEntry()
        self.writeNumProcEntry()
        self.writeIPdracAddress()
        self.writeIPaddress1()
        self.writeIPaddress2()
        self.root.title(newTitle)
        # color = self.var.get()
        # self.root['bg'] = color
    def clearFunc(self):
        self.add.select()
        self.numHDDentry.delete(0,END)
        self.sizeHDDentry.delete(0,END)
        self.memEntry.delete(0,END)
        self.numProcEntry.delete(0,END)
        self.IPdracEntry.delete(0,END)
        self.ip1Entry.delete(0,END)
        self.ip2Entry.delete(0,END)
        self.descriptionEntry.delete(0,END)
        self.serviceTagEntry.delete(0,END)
        self.var.set('Server Model')
    def writeNumHDDentry(self):
        try:
            assert int(self.numHDDentry.get())
            val1 = self.numHDDentry.get()
            WRITE()
        except Exception as invalid:
            self.numHDDentry.delete(0,END)
            self.numHDDentry.insert(0,"requires integer")
    def writeSizeHDDentry(self):
        try:
            assert int(self.sizeHDDentry.get())
            val1 = self.sizeHDDentry.get()
            print val1
        except Exception as invalid:
            self.sizeHDDentry.delete(0,END)
            self.sizeHDDentry.insert(0,"requires integer")
    def writeMemEntry(self):
        try:
            assert int(self.memEntry.get())
            val1 = self.memEntry.get()
            print val1
        except Exception as invalid:
            self.memEntry.delete(0,END)
            self.memEntry.insert(0,"requires integer")
    def writeNumProcEntry(self):
        try:
            assert int(self.numProcEntry.get())
            val1 = self.numProcEntry.get()
            print val1
        except Exception as invalid:
            self.numProcEntry.delete(0,END)
            self.numProcEntry.insert(0,"requires integer")
    def writeIPdracAddress(self):
        try:
            assert int(self.IPdracEntry.get())
            val1 = self.IPdracEntry.get()
            print val1
        except Exception as invalid:
            self.IPdracEntry.delete(0,END)
            self.IPdracEntry.insert(0,"requires ip address")
    def writeIPaddress1(self):
        try:
            assert int(self.ip1Entry.get())
        except Exception as invalid:
            self.ip1Entry.delete(0,END)
            self.ip1Entry.insert(0,"requires ip address")
    def writeIPaddress2(self):
        try:
            assert int(self.ip2Entry.get())
        except Exception as invalid:
            self.ip2Entry.delete(0,END)
            self.ip2Entry.insert(0,"requires ip address")
    def writeDescriptionEntry(self):
        description = self.descriptionEntry.get()
    def writeServiceTagEntry(self):
        servicetag = self.serviceTagEntry.get()
    def WRITE(self):
        a=1


print __name__
if __name__ == "__main__":
    print "please launch using blah blah"
    form = InvForm()
    form()
__author__ = 'root'
from Tkinter import *
from modules.valid_IP import *
# from anydbm import *
class InvForm:
    def __init__(self):
        self.root = Tk()
        self.root.title("Inventory Application Form")
        self.choices = []
        self.drawEntries()
        self.drawDescription()
        self.drawBottomButtons()
        self.drawServerDelete()
        self.drawServerAdd()
        self.root.mainloop()
    def drawEntries(self):
        self.informationFrame = Frame(bd=3,relief=RIDGE,padx=10)
        self.informationFrame.grid(row=1,column=0,rowspan=7,columnspan=2)
        #drop down lists
        self.serverDropDown()
        #regular entries
        self.numHDDlabel = Label(self.informationFrame, text = "Number of HDDs:").grid(row=2,column=0)
        self.numHDDentry = Entry(self.informationFrame)
        self.numHDDentry.grid(row=2, column = 1)
        self.sizeHDDlabel = Label(self.informationFrame, text = "Size of HDDs:").grid(row=3,column=0)
        self.sizeHDDentry = Entry(self.informationFrame)
        self.sizeHDDentry.grid(row=3, column = 1)
        self.memLabel = Label(self.informationFrame, text = "Memory:").grid(row=4,column=0)
        self.memEntry = Entry(self.informationFrame)
        self.memEntry.grid(row=4, column = 1)
        self.numProcLabel = Label(self.informationFrame, text = "Processors:").grid(row=5,column=0)
        self.numProcEntry = Entry(self.informationFrame)
        self.numProcEntry.grid(row=5, column = 1)
        self.IPdracLabel = Label(self.informationFrame,text = "DRAC IP address:").grid(row=6,column=0)
        self.IPdracEntry = Entry(self.informationFrame)
        self.IPdracEntry.grid(row=6,column=1)
        self.ip1Label = Label(self.informationFrame,text = "IP address 1:").grid(row=7,column=0)
        self.ip1Entry = Entry(self.informationFrame)
        self.ip1Entry.grid(row=7,column=1)
        self.ip2Label = Label(self.informationFrame,text = "IP address 2:").grid(row=8,column=0)
        self.ip2Entry = Entry(self.informationFrame)
        self.ip2Entry.grid(row=8,column=1)
        self.serviceTagLabel = Label(self.informationFrame,text="Service Tag:").grid(row=9,column=0)
        self.serviceTagEntry = Entry(self.informationFrame)
        self.serviceTagEntry.grid(row=9,column=1)
    def serverDropDown(self):
        self.serverLabel = Label(self.informationFrame,text="Server Model:").grid(row=0,column=0)
        self.serverString = StringVar(self.root)
        self.serverString.set('Server Model')
        self.serverModels = ['R610','R710','R720','R620','R630','R730XD']
        for server in self.serverModels:
            self.choices.insert(0,server)
        # I think you can put all 3 lines on one line, more readable (JN)
        self.serverOption = OptionMenu(self.informationFrame,self.serverString,*self.choices)
        self.serverOption.config(width=14)
        self.serverOption.grid(row=0, column=1, columnspan=2)
        #firmware dropdown list
        self.firmwareLabel = Label(self.informationFrame,text="Firmware version:").grid(row=1,column=0)
        self.firmwareString = StringVar(self.root)
        self.firmwareString.set('Firmware Version')
        self.firmwareOption = OptionMenu(self.informationFrame,self.firmwareString,self.firmwareList())
        self.firmwareOption.config(width=14)
        self.firmwareOption.grid(row=1,column=1)
    def drawDescription(self):
        self.descriptionFrame = Frame(bd=3,relief=RIDGE)
        self.descriptionFrame.grid(row=1,column=2,rowspan=7,sticky=N+S)
        self.descriptionLabel = Label(self.descriptionFrame,text="Description:").grid(row=1,column=2)
        self.descriptionEntry = Entry(self.descriptionFrame)
        self.descriptionEntry.grid(row=2,column=2,rowspan=7,sticky=N+S)
        self.descriptionEntry.insert(0,"needs formatting/wordwrap")
    def drawBottomButtons(self):
        self.bottomButtonFrame = Frame(bd=3,relief=RIDGE)
        self.bottomButtonFrame.grid(row=10,column=0,columnspan=3)
        self.closeButton = Button(self.bottomButtonFrame, text = "Exit", command=self.closeFunc,width=17).grid(row=0, column = 2)
        self.applyButton = Button(self.bottomButtonFrame,text="Apply",command=self.applyFunc,width=16).grid(row=0,column=1)
        self.clearButton = Button(self.bottomButtonFrame,text="Clear",command=self.clearFunc,width=17).grid(row=0,column=0)
    def drawServerAdd(self):
        self.serverAddFrame = Frame(bd=3,relief=RIDGE)
        self.serverAddFrame.grid(row=1,column=3,rowspan=2)
        self.serverAddLabel = Label(self.serverAddFrame,text="Add Server Model").grid(row=0,column=0)
        self.serverAddEntry = Entry(self.serverAddFrame)
        self.serverAddEntry.grid(row=1,column=0)
        self.serverAddButton = Button(self.serverAddFrame,text="Add Server",command=self.serverAdd,width=16).grid(row=2,column=0)
        self.redrawServerList()
    def drawServerDelete(self):
        self.serverDeleteFrame = Frame(bd=3,relief=RIDGE)
        self.serverDeleteFrame.grid(row=3,column=3,rowspan=2)
        self.serverDeleteString = StringVar(self.serverDeleteFrame)
        self.serverDeleteString.set(self.choices[0])
        self.serverDeleteLabel = Label(self.serverDeleteFrame,text="Delete Server Model").grid(row=0,column=0)
        self.serverDeleteOption = OptionMenu(self.serverDeleteFrame,self.serverDeleteString,*self.choices)
        self.serverDeleteOption.config(width=14)
        self.serverDeleteOption.grid(row=0, column=0)
        self.serverDeleteButton = Button(self.serverDeleteFrame,text="Delete Server",command=self.serverDelete,width=16).grid(row=2,column=0)
    def closeFunc(self):
        print "Thank you for using the Inventory Application Form"
        self.root.destroy()
    def applyFunc(self):
        newTitle = "Server is %s." % self.serverString.get()
        self.writeNumHDDentry()
        self.writeSizeHDDentry()
        self.writeMemEntry()
        self.writeNumProcEntry()
        self.writeIPdracAddress()
        self.writeIPaddress1()
        self.writeIPaddress2()
        self.root.title(newTitle)
        # color = self.serverString.get()
        # self.root['bg'] = color
    def clearFunc(self):
        # self.add.select()
        self.numHDDentry.delete(0,END)
        self.sizeHDDentry.delete(0,END)
        self.memEntry.delete(0,END)
        self.numProcEntry.delete(0,END)
        self.IPdracEntry.delete(0,END)
        self.ip1Entry.delete(0,END)
        self.ip2Entry.delete(0,END)
        self.descriptionEntry.delete(0,END)
        self.serviceTagEntry.delete(0,END)
        self.serverString.set('Server Model')
        self.firmwareString.set('Firmware Version')
    def writeNumHDDentry(self):
        try:
            print self.numHDDentry.get()
            assert int(self.numHDDentry.get())
            val1 = self.numHDDentry.get()
            # WRITE()
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
    def serverAdd(self):
        if self.serverAddEntry.get() != "":
            server = self.serverAddEntry.get()
            self.serverAddEntry.delete(0,END)
            self.choices.insert(0,server)
            self.redrawServerList()
    def serverDelete(self):
        server = self.serverDeleteString.get()
        try:
            index = self.choices.index(server)
            self.choices.pop(index)
        except Exception as Error:
            print Error
        self.redrawServerList()
    def redrawServerList(self):
        self.serverDeleteString.set('Server Model')
        self.serverDeleteOption = OptionMenu(self.serverDeleteFrame,self.serverDeleteString,*self.choices)
        self.serverDeleteOption.config(width=14)
        self.serverDeleteOption.grid(row=0, column=0)
        self.serverString.set('Server Model')
        self.serverOption = OptionMenu(self.informationFrame,self.serverString,*self.choices)
        self.serverOption.config(width=14)
        self.serverOption.grid(row=0, column=1, columnspan=2)
    def firmwareList(self):
        server = self.serverString.get()
    def writeDescriptionEntry(self):
        description = self.descriptionEntry.get()
    def writeServiceTagEntry(self):
        servicetag = self.serviceTagEntry.get()
    def WRITE(self):
        a=1
if __name__ == "__main__":
    # print "please launch using blah blah"
    # def form():
    #     form = InvForm()
    # form()
    InvForm()
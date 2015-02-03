__author__ = 'quicksand77'
from Tkinter import *
from modules.valid_IP import *
from DataDB import *
class InvForm:
    def __init__(self):
        self.validateIP = CheckIP()
        self.root = Tk()
        self.root.title("Inventory Application Form")
        self.root.resizable(width=False, height=False)
        self.modelChoices = []
        self.firmwareVersions = []
        self.drawEntries()
        self.drawDescription()
        self.drawBottomButtons()
        self.drawServerDelete()
        self.drawServerAdd()
        self.drawFirmwareDelete()
        self.drawFirmwareAdd()
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
            self.modelChoices.insert(0,server)
        # I think you can put all 3 lines on one line, more readable (JN)
        self.serverOption = OptionMenu(self.informationFrame,self.serverString,*self.modelChoices)
        self.serverOption.config(width=14)
        self.serverOption.grid(row=0, column=1, columnspan=2)
        #firmware dropdown list
        self.firmwareLabel = Label(self.informationFrame,text="Firmware version:").grid(row=1,column=0)
        self.firmwareString = StringVar(self.root)
        self.firmwareString.set('Firmware Version')
        self.firmwareVersionList = ['Version1','Version2','Version3','Version4','Version5','Version6']
        for firmChoice in self.firmwareVersionList:
            self.firmwareVersions.insert(0,firmChoice)
        self.firmwareOption = OptionMenu(self.informationFrame,self.firmwareString,*self.firmwareVersions)
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
        # self.redrawServerList()
    def drawServerDelete(self):
        self.serverDeleteFrame = Frame(bd=3,relief=RIDGE)
        self.serverDeleteFrame.grid(row=3,column=3,rowspan=3)
        # self.serverDeleteLabel = Label(self.serverDeleteFrame,text="Delete Server Model").grid(row=0,column=0)
        self.serverDeleteString = StringVar(self.serverDeleteFrame)
        self.serverDeleteString.set(self.modelChoices[0])
        self.serverDeleteLabel = Label(self.serverDeleteFrame,text="Delete Server Model").grid(row=0,column=0)
        self.serverDeleteOption = OptionMenu(self.serverDeleteFrame,self.serverDeleteString,*self.modelChoices)
        self.serverDeleteOption.config(width=14)
        self.serverDeleteOption.grid(row=1, column=0)
        self.serverDeleteButton = Button(self.serverDeleteFrame,text="Delete Server",command=self.serverDelete,width=16,padx=2).grid(row=2,column=0)
    def drawFirmwareAdd(self):
        self.firmwareAddFrame = Frame(bd=3,relief=RIDGE)
        self.firmwareAddFrame.grid(row=1,column=4,rowspan=2)
        self.firmwareAddLabel = Label(self.firmwareAddFrame,text="Add Firmware Version").grid(row=0,column=0)
        self.firmwareAddEntry = Entry(self.firmwareAddFrame)
        self.firmwareAddEntry.grid(row=1,column=0)
        self.firmwareAddButton = Button(self.firmwareAddFrame,text="Add Firmware",command=self.serverAdd,width=16,padx=2).grid(row=2,column=0)
        self.redrawFirmwareList("a")
    def drawFirmwareDelete(self):
        self.firmwareDeleteFrame = Frame(bd=3,relief=RIDGE)
        self.firmwareDeleteFrame.grid(row=3,column=4,rowspan=3)
        # self.firmwareDeleteLabel = Label(self.firmwareDeleteFrame,text="Delete firmware Model").grid(row=0,column=0)
        self.firmwareDeleteString = StringVar(self.firmwareDeleteFrame)
        self.firmwareDeleteString.set(self.firmwareVersions[0])
        self.firmwareDeleteLabel = Label(self.firmwareDeleteFrame,text="Delete firmware Model").grid(row=0,column=0)
        self.firmwareDeleteOption = OptionMenu(self.firmwareDeleteFrame,self.firmwareDeleteString,*self.firmwareVersions)
        self.firmwareDeleteOption.config(width=14)
        self.firmwareDeleteOption.grid(row=1, column=0)
        self.firmwareDeleteButton = Button(self.firmwareDeleteFrame,text="Delete firmware",command=self.firmwareDelete,width=16,padx=2).grid(row=2,column=0)
        self.redrawFirmwareList("a")
    def closeFunc(self):
        print "Thank you for using the Inventory Application Form"
        self.root.destroy()
    def applyFunc(self):
        newTitle = "Server is %s." % self.serverString.get()
        self.root.title(newTitle)
        s1 = self.getServiceTagEntry()
        s2 = self.serverString.get()
        s3 = self.firmwareString.get()
        s4 = self.getNumHDDEntry()
        s5 = self.getSizeHDDEntry()
        s6 = self.getMemEntry()
        s7 = self.getNumProcEntry()
        s8 = self.getDracIPaddress()
        s9 = self.getIPaddress1()
        s10 = self.getIPaddress2()
        s11 = self.getDescriptionEntry()
        print s1,",",s2,",",s3,",",s4,",",s5,",",s6,",",s7,",",s8,",",s9,",",s10,",",s11
        self.WRITE(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11)
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
    def getNumHDDEntry(self):
        try:
            assert int(self.numHDDentry.get())
            val1 = self.numHDDentry.get()
            return val1
        except Exception as invalid:
            self.numHDDentry.delete(0,END)
            self.numHDDentry.insert(0,"requires integer")
    def getSizeHDDEntry(self):
        try:
            assert int(self.sizeHDDentry.get())
            val1 = self.sizeHDDentry.get()
            return val1
        except Exception as invalid:
            self.sizeHDDentry.delete(0,END)
            self.sizeHDDentry.insert(0,"requires integer")
    def getMemEntry(self):
        try:
            assert int(self.memEntry.get())
            val1 = self.memEntry.get()
            return val1
        except Exception as invalid:
            self.memEntry.delete(0,END)
            self.memEntry.insert(0,"requires integer")
    def getNumProcEntry(self):
        try:
            assert int(self.numProcEntry.get())
            val1 = self.numProcEntry.get()
            return val1
        except Exception as invalid:
            self.numProcEntry.delete(0,END)
            self.numProcEntry.insert(0,"requires integer")
    def getDracIPaddress(self):
        try:
            assert self.validateIP.checkip(self.IPdracEntry.get())
            val1 = self.IPdracEntry.get()
            return val1
        except Exception as invalid:
            print invalid
            self.IPdracEntry.delete(0,END)
            self.IPdracEntry.insert(0,"requires ipv4/ipv6")
    def getIPaddress1(self):
        try:
            assert self.validateIP.checkip(self.ip1Entry.get())
            val1 = self.ip1Entry.get()
            return val1
        except Exception as invalid:
            self.ip1Entry.delete(0,END)
            self.ip1Entry.insert(0,"requires ipv4/ipv6")
    def getIPaddress2(self):
        try:
            assert self.validateIP.checkip(self.ip2Entry.get())
            val1 = self.ip2Entry.get()
            return val1
        except Exception as invalid:
            self.ip2Entry.delete(0,END)
            self.ip2Entry.insert(0,"requires ipv4/ipv6")
    def getDescriptionEntry(self):
        description = self.descriptionEntry.get()
        return description
    def getServiceTagEntry(self):
        servicetag = self.serviceTagEntry.get()
        return servicetag
    def serverAdd(self):
        if self.serverAddEntry.get() != "":
            server = self.serverAddEntry.get()
            self.serverAddEntry.delete(0,END)
            self.modelChoices.insert(0,server)
            self.redrawServerList("a")
    def serverDelete(self):
        server = self.serverDeleteString.get()
        try:
            index = self.modelChoices.index(server)
            popped = self.modelChoices.pop(index)
        except Exception as Error:
            print Error
        self.redrawServerList(popped)
    def redrawServerList(self,popped):
        if popped != "a":
            self.serverDeleteString.set('Deleted '+popped+'.')
        self.serverDeleteOption = OptionMenu(self.serverDeleteFrame,self.serverDeleteString,*self.modelChoices)
        self.serverDeleteOption.config(width=14)
        self.serverDeleteOption.grid(row=1, column=0)
        self.serverString.set('Server Model')
        self.serverOption = OptionMenu(self.informationFrame,self.serverString,*self.modelChoices)
        self.serverOption.config(width=14)
        self.serverOption.grid(row=0, column=1, columnspan=2)
    def firmwareAdd(self):
        if self.firmwareAddEntry.get() != "":
            version = self.firmwareAddEntry.get()
            self.firmwareAddEntry.delete(0,END)
            self.firmwareVersions.insert(0,version)
            self.redrawFirmwareList("a")
    def firmwareDelete(self):
        version = self.firmwareDeleteString.get()
        try:
            index = self.firmwareVersions.index(version)
            popped = self.firmwareVersions.pop(index)
        except Exception as Error:
            print Error
        self.redrawFirmwareList(popped)
    def redrawFirmwareList(self,popped):
        if popped != "a":
            self.firmwareDeleteString.set('Deleted '+popped+'.')
        self.firmwareDeleteOption = OptionMenu(self.firmwareDeleteFrame,self.firmwareDeleteString,*self.firmwareVersions)
        self.firmwareDeleteOption.config(width=14)
        self.firmwareDeleteOption.grid(row=1, column=0)
        self.firmwareDeleteButton = Button(self.firmwareDeleteFrame,text="Delete firmware",command=self.firmwareDelete,width=16,padx=2).grid(row=2,column=0)
        self.firmwareString.set('Firmware Version')
        self.firmwareOption = OptionMenu(self.informationFrame,self.firmwareString,*self.firmwareVersions)
        self.firmwareOption.config(width=14)
        self.firmwareOption.grid(row=1,column=1)
    def firmwareList(self):
        server = self.serverString.get()
        if server == 'Server Model':
            self.firmwareString.set('Firmware Version')
        for servers in self.modelChoices:
            self.firmwareString.set(self.serverFirmware()+'firm')
    def serverFirmware(self):
        return self.serverString.get()
    def WRITE(self,serviceTag,model,firmware,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description):
        dbConnection = DataDB()
        self.__dbConnection = dbConnection
        try:
            dbConnection.open("serverTable.db")
            serviceTag = self.__dbConnection.read(self.getID())
        except Exception as e:
            print e
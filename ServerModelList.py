__author__ = 'quicksand77'
import os
class ServerModelList:
    def __init__(self):
        # self.defaults = ["R610", "R710", "R720", "R620", "R730", "R630", "R730XD"]
        self.defaults = ["test1", "test2", "test3", "test4"]
        self.createServerModelListFile()
        self.check()
    def check(self):
        with open(self.path,"r+") as f:
            a = f.readlines()
        if len(a) == 0:
            self.addToFile(self.defaults)
    def getList(self):
        serverList = []
        with open(self.path, "r+") as f:
            for line in f:
                serverList.append(line.strip())
        return serverList
    def addToFile(self,modelChoices):
        with open(self.path,"a") as f:
            for thing in modelChoices:
                f.write(thing+"\n")
    def removeFromFile(self,poppedList):
        in1 = open(self.path)
        out1 = open(self.path + ".new", "w")
        list1 = []
        for i in in1.readlines():
            print i
        if len(poppedList) > 0:
            for pop in poppedList:
                for i in in1.readlines():
                    if i.strip() == pop:
                        list1.append(i)
                    else:
                        print "out: "+pop
                        out1.write(i)
        in1.close()
        out1.close()
        os.remove(self.path)
        os.rename(self.path + ".new", self.path)
        if len(list1) != 0:
            print "removed",list1
    def createServerModelListFile(self):
        try:
            #windows dir path
            path = ".\modules"
            if not os.path.isdir(path):
                os.makedirs(path)
                print "Created directory: '%s'."%path
        except:
            #linux dir path
            path = "./modules"
            if not os.path.isdir(path):
                os.makedirs(path)
                print "Created directory: '%s'."%path
        try:
            #windows file path
            path = ".\modules\serverModelList.txt"
            if not os.path.exists(path):
                file1 = open(path,"w")
                self.addToFile(self.defaults)
                file1.close()
                print "Created file: '%s'."%path
        except:
            #linux file path
            path = "./modules/serverModelList.txt"
            if not os.path.exists(path):
                file1 = open(path,"w")
                self.addToFile(self.defaults)
                file1.close()
                print "Created file: '%s'."%path
        if os.path.exists(".\modules\serverModelList.txt"):
            self.path = ".\modules\serverModelList.txt"
            self.isWindows = True
        else:
            self.path = "./modules/serverModelList.txt"
            self.isWindows = False
ServerModelList()
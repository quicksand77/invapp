__author__ = 'quicksand77'
__author__ = 'jeff'
import sqlite3
import os
class DataDB:
    def __init__(self):
        self.__wasOpened = False
    def open(self, path):
        self.__path = path
        self.__conn = sqlite3.connect(self.__path)
        self.__cur = self.__conn.cursor()
        if os.path.getsize(self.__path) == 0:
            self.create()
        try:
            self.__conn = sqlite3.connect(self.__path)
            self.__cur = self.__conn.cursor()
        except:
            print "Database file not found, creating..."
            self.create()
            self.__conn = sqlite3.connect(self.__path)
            self.__cur = self.__conn.cursor()

        self.__wasOpened = True
    def create(self):
        print "creating database table 'serverTable'"
        createTable = """CREATE TABLE serverTable(
                         ID VARCHAR primary key, serverModel VARCHAR,
                         firmwareVersion VARCHAR, numHDD VARCHAR,
                         sizeHDD VARCHAR, mem VARCHAR, proc VARCHAR,
                         dracIP VARCHAR, ip1 VARCHAR, ip2 VARCHAR,
                         description VARCHAR)"""
        self.__cur.execute(createTable)
        self.__conn.commit()
    def insert(self,id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description):
        try:
            r = (id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description)
            self.__cur.execute('INSERT INTO serverTable VALUES (?,?,?,?,?,?,?,?,?,?,?)', r)
            self.__conn.commit()
            print "insert try"
        except Exception as e:
            self.update(id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description)
            print "insert exception"
            print e

    def update(self,id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description):
        print "update"
        s1 = (serverModel, id)
        s2 = (firmwareVersion, id)
        s3 = (numHDD,id)
        s4 = (sizeHDD,id)
        s5 = (mem,id)
        s6 = (proc,id)
        s7 = (dracIP,id)
        s8 = (ip1,id)
        s9 = (ip2,id)
        s10 = (description,id)
        self.__cur.execute('UPDATE serverTable SET serverModel = ? WHERE ID = ?',s1)
        self.__cur.execute('UPDATE serverTable SET firmwareVersion = ? WHERE ID = ?',s2)
        self.__cur.execute('UPDATE serverTable SET numHDD = ? WHERE ID = ?',s3)
        self.__cur.execute('UPDATE serverTable SET sizeHDD = ? WHERE ID = ?',s4)
        self.__cur.execute('UPDATE serverTable SET mem = ? WHERE ID = ?',s5)
        self.__cur.execute('UPDATE serverTable SET proc = ? WHERE ID = ?',s6)
        self.__cur.execute('UPDATE serverTable SET dracIP = ? WHERE ID = ?',s7)
        self.__cur.execute('UPDATE serverTable SET ip1 = ? WHERE ID = ?',s8)
        self.__cur.execute('UPDATE serverTable SET ip2 = ? WHERE ID = ?',s9)
        self.__cur.execute('UPDATE serverTable SET description = ? WHERE ID = ?',s10)
        self.__conn.commit()
    def read(self, id):
        t = (id,)
        for row in self.__cur.execute('SELECT * FROM serverTable WHERE ID = ?',t):
            # # print "here2"
		    # print(row[1])
            print "read"
    def currentConfig(self):
        for row in self.__cur.execute('SELECT * FROM serverTable'):
            print row
            print "currentconfig"
    def close(self,id):
            if self.__wasOpened:
                self.read(id)
                self.__cur.close()
                self.__conn.close()
if __name__ == "__main__":
    print("Please launch using 'main.py")
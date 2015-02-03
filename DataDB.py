__author__ = 'quicksand77'
__author__ = 'jeff'

import sqlite3
import os
# from datetime import time, date, datetime
# import time

class DataDB:

    def __init__(self):
        self.__wasOpened = False
        hr24 = ('%H:%M:%S')
        self.__hr24 = hr24
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
                         description VARCHAR, updated_at TIME)"""
        self.__cur.execute(createTable)
        self.__conn.commit()


    def insert(self,id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description,hrformat):
        now = time.strftime("%c")
        try:
            r = (id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description,now)
            self.__cur.execute('INSERT INTO serverTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', r)
            self.__conn.commit()
        # except Exception as e:
        #     print str(e)
        except:
            self.update(id,hrformat)


    def update(self,id,serverModel,firmwareVersion,numHDD,sizeHDD,mem,proc,dracIP,ip1,ip2,description,hrformat):
        # now = time.strftime("%c")
        s1 = (serverModel, id)
        s2 = (firmwareVersion, id)
        s3 = (sizeHDD,id)
        s4 = (mem,id)
        s5 = (proc,id)
        s6 = (dracIP,id)
        s7 = (ip1,id)
        s8 = (ip2,id)
        s9 = (description,id)
        v = (hrformat, id)
        # n = (now, id)
        self.__cur.execute('UPDATE serverTable SET serverModel = ? WHERE ID = ?',s1)
        self.__cur.execute('UPDATE serverTable SET firmwareVersion = ? WHERE ID = ?',s2)
        self.__cur.execute('UPDATE serverTable SET sizeHDD = ? WHERE ID = ?',s3)
        self.__cur.execute('UPDATE serverTable SET mem = ? WHERE ID = ?',s4)
        self.__cur.execute('UPDATE serverTable SET proc = ? WHERE ID = ?',s5)
        self.__cur.execute('UPDATE serverTable SET dracIP = ? WHERE ID = ?',s6)
        self.__cur.execute('UPDATE serverTable SET ip1 = ? WHERE ID = ?',s7)
        self.__cur.execute('UPDATE serverTable SET ip2 = ? WHERE ID = ?',s8)
        self.__cur.execute('UPDATE serverTable SET description = ? WHERE ID = ?',s9)
        self.__cur.execute('UPDATE serverTable SET hrformat = ? WHERE ID = ?', v )
        # self.__cur.execute('UPDATE clockdb SET updated_at = ? WHERE ID = ?', n)
        self.__conn.commit()


    def read(self, id):
        t = (id,)
        # print("Currently configured clocks")
        # for row in self.__cur.execute('SELECT * FROM clockdb'):
        #     print(row)

        for row in self.__cur.execute('SELECT * FROM serverTable WHERE ID = ?', t):
            # print("Current default setting for clock # %s is %s" % (row[0], row[1]))
            return row[1]

        # value = self.__cur.execute('SELECT * FROM clockdb WHERE ID = ?', t)
        # print(value)
        # self.close(id)
    def close(self,id):
            if self.__wasOpened:
                self.read(id)
                self.__cur.close()
                self.__conn.close()
'''
    def currentConfig(self):
        # print("Currently configured clocks")
        for row in self.__cur.execute('SELECT * FROM clockdb'):
            # print(row)
            if row[1] == self.__hr24:
                # print("Clock #%s - 24 hour format" % row[0])
                print("Clock #%s --> 24 hour format, last updated %s "% (row[0], str(row[2])))
            elif row[1] == self.__hr12:
                # print("Clock #%s - 12 hour format" % row[0], )
                # print("Last updated at: %s "% str(row[2]))
                print("Clock #%s --> 12 hour format, last updated %s "% (row[0], str(row[2])))
'''


if __name__ == "__main__":
    print("Please launch using 'main.py")
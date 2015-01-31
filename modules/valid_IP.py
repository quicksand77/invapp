__author__ = 'jeff'
import ipaddress

class CheckIP:

    def checkip(self):
        addr = raw_input("Please enter a valid IP address: \n")
        try:
            ipaddress.ip_address(addr)
            print "success"
        except:
            print "Please enter a valid IP address"
            self.checkip()

if __name__ == "__main__":
    verify = CheckIP()
    verify.checkip()
__author__ = 'jeff'
import ipaddress

class CheckIP:
    def checkip(self,ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False


# added as a sanity check (JN)
if __name__ == "__main__":
    print "launch IP checker"
    localCheck = CheckIP()
    testIP = raw_input("please enter an IP address for me to check: \n")
    print localCheck.checkip(testIP)
    while testIP != "quit":
        testIP = raw_input("please enter an IP address for me to check('quit' to exit): \n")
        if testIP == 'quit':
            continue
        print localCheck.checkip(testIP)
    print "closed IP checker"
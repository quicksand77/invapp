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
    localCheck = CheckIP()
    testIP = raw_input("please enter an IP address for me to check: \n")
    print localCheck.checkip(testIP)

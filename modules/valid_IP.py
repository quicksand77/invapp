__author__ = 'jeff'
import ipaddress

class CheckIP:
    def checkip(self,ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False
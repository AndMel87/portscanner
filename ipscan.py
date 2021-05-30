# IP Scanner 2021

#--- Libraries ---
import portscanner

ip = input("What is the IP or address of the site you would like to scan?")
portscanner.scan(ip)

# --- Libraries ---
import socket
from IPy import IP

#scan function
def scan(target):
    convertedIP = checkIP(target)
    print("\n" + "Scanning target(s)..." + str(target))
    #scan ports in range
    for port in range(1, 500):
        scanPort(convertedIP, port)


#Function to convert to IP-format. Function "IP" takes parametre "ip". If IP is correct, return the IP. If not, try to resolve IP by hostname input "ip"
def checkIP(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


#get port banner, s.recv(bytes)
def getBanner(s):
    return s.recv(1024)


#Establish connection with target machine
#try and except rule
def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        #set timeout, half a second. Less accurate, but faster
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = getBanner(sock)
            #.decode is a function that automatically decodes
            print("[+] Open port " + str(port) + " : " + str(banner.decode().strip("\n")))
        except:
            print("[+] Open port " + str(port))
    except:
        pass

#input from user. Target or targets.
#if __name__=="__main__": code is only run within this program, not when importing libraries
if __name__=="__main__":
    targets = input("[+] Enter target(s) to scan (split multiple with ,): ")
    if "," in targets:
        for ipAdd in targets.split(","):
            scan(ipAdd.strip(" "))
    else:
        scan(targets)

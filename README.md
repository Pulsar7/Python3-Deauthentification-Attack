# Python3-Deauthentification-Attack
Python3 Programming 
Das Script greift auf das "Scapy" -Modul von Python3 zu und sendet bestimmte Packete zu einer BSSID, bis diese nicht mehr 
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


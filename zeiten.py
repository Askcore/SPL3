# zeiten.py 

import sys

def zeitInSekunden(h, m, s):
    return int(s) + int(m)*60 + int(h)*3600

#beginnZeit = input("Beginnzeit: ")
#endeZeit = input("Endzeit: ")

# Zeit im Format HH:MM:SS

p = sys.argv

beginnZeit = p[1]
endeZeit = p[2]

beginn = beginnZeit.split(":")
ende = endeZeit.split(":")

zeit = zeitInSekunden(ende[0], ende[1], ende[2]) - zeitInSekunden(beginn[0], beginn[1], beginn[2])

print(zeit)
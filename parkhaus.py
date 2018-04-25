# parkhaus.py 
# Angabe fuer das Beispiel: siehe Moodle

print("Linienbus-Simulator")
h = input("Wie viele Haltestellen soll es geben? ")
h = int(h)
personen = 0
i = 0

print("Der Bus fährt los.\n")

while (i < h):
    i = i+1
    print("Der Bus ist in Haltestelle ",h,".",sep="")
    einstieg = input("Wie viele Personen steigen ein? ")
    einstieg = int(einstieg)
    personen = personen + einstieg
    ausstieg = input("Wie viele Personen steigen aus? ")
    ausstieg = int(ausstieg)
    personen = personen - ausstieg
    if (personen > 60):
        print("Es sind zu viele Personen im Bus, Sie müssen",personen-60,"Personen da lassen!")
        personen = 60
    elif(personen < 0):
        print("Es steigen mehr Personen ein als aus.Es sind nur",personen + ausstieg,"im Bus. Geben Sie nochmal ein!")
        i = i-1
    else:
        print("Es sind ",personen,"Personen im Bus.\n")
print("Der Bus hat die Endstation erreicht.")
print("'Bitt alle aussteigen!'")
oreP = [10, 11,13,15,17]
oreA = [11,14,18,19,20]
destinazioni = ["Roma", "Milano", "Parigi", "Praga", "Berlino"]

destinazione=str(input("Inserisci una destinazione per controllare gli orari dei voli: "))
intervallo_di_tempo=int(input("Inserisci un intervallo di tempo:"))
if(oreP==intervallo_di_tempo):
    print(oreP)
elif(oreA==intervallo_di_tempo):
    print(oreA)
else:
    print(destinazione)

    
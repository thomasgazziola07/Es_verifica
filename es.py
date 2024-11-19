voto1= float(input("Inserisci il primo voto:"))
voto2= float(input("Inserisci il secondo voto:"))
voto3= float(input("Inserisci il terzo voto:"))
print("Vuoi la media in decimi o in centesimi?(1=decimi,2=centesimi)")
scelta= int(input())
if(scelta==1):
    media=voto1+voto2+voto3/3
    print(media)
elif(scelta==2):
    media=voto1+voto2+voto3/3
    media=media*100/10
    print(media)


lanci= int("Inserisci il numero dei lanci:")
if(lanci <= 5):
    lunghezza_lanci = int("Inserisci la lunghezza dei lanci:")
    media=lunghezza_lanci/lanci
    print(media)



anni_di_servizio = int(input("Inserisci quanti anni di servizio hai svolto:"))
if(anni_di_servizio == 1):
    livello_programmatore = int(input("Inserisci il tuo livello programmatore(1-3):"))
    if(livello_programmatore==1):
        bonus_produttività = 100
        print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==2):
            bonus_produttività=200
            print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==3):
            bonus_produttività=300
            print("Il tuo bonus produttività è di: ",bonus_produttività)

if(1<anni_di_servizio<=3 ):
    livello_programmatore = int(input("Inserisci il tuo livello programmatore(1-3):"))
    if(livello_programmatore==1):
        bonus_produttività = 200
        print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==2):
            bonus_produttività=300
            print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==3):
            bonus_produttività=400
            print("Il tuo bonus produttività è di: ",bonus_produttività)

if(3<anni_di_servizio<=5 ):
    livello_programmatore = int(input("Inserisci il tuo livello programmatore(1-3):"))
    if(livello_programmatore==1):
        bonus_produttività = 300
        print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==2):
            bonus_produttività=400
            print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==3):
            bonus_produttività=500
            print("Il tuo bonus produttività è di: ",bonus_produttività)

if(5<anni_di_servizio<=7 ):
    livello_programmatore = int(input("Inserisci il tuo livello programmatore(1-3):"))
    if(livello_programmatore==1):
        bonus_produttività = 400
        print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==2):
            bonus_produttività=500
            print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==3):
            bonus_produttività=600
            print("Il tuo bonus produttività è di: ",bonus_produttività)

if(7<anni_di_servizio ):
    livello_programmatore = int(input("Inserisci il tuo livello programmatore(1-3):"))
    if(livello_programmatore==1):
        bonus_produttività = 500
        print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==2):
            bonus_produttività=600
            print("Il tuo bonus produttività è di: ",bonus_produttività)
    elif(livello_programmatore==3):
            bonus_produttività=700
            print("Il tuo bonus produttività è di: ",bonus_produttività)
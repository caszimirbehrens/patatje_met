dict = {"eerstewoord": "hello"}

def oplezen():
    for key in dict:
        print(str(key) + ": " + str(dict[key]))
    start()
    
def toevoegen(woord1, woord2):
    dict[woord1] = woord2
    print(woord1 + " is toegevoegt aan de dictionairy")
    start()
    
def verwijderen(woord3):
    if woord3 in dict:
        del dict[woord3]
        print(woord3 + " is verwijdert")
        start()
    else:
        print("die key zit niet in de dictionairy")
        start()
        
def opslaan(file_naam):
    naam = file_naam+".txt"
    file = open(naam,"w+")
    file.write("deze file is de dictionairy van " + je_naam+":\n")
    file.write("----------------------------------\n")
    for key in dict:
         file.write(str(key) + ": " + str(dict[key])+"\n")
    file.write("----------------------------------\n")
    file.close()
    print(file_naam + " is nu aangemaakt")
        

def start():
    print("--------------------------------------")
    print("1: dictionairy oplezen")
    print("2: woord toevoegen aan dictionairy")
    print("3: woord verwijderen uit dictionairy")
    print("4: dictionairy opslaan")
    print("--------------------------------------")
    keuze = int(input("wat wil je doen? "))
    if keuze == 1:
        print("dictionairy oplezen")
        oplezen()
        
    elif keuze == 2:
        woordje1 = input("wat woord de key? ")
        woordje2 = input("wat woord de value? ")
        toevoegen(woordje1, woordje2)
    elif keuze == 3:
        woordje3 = input("welke key wil je verwijderen? ")
        verwijderen(woordje3)
    elif keuze == 4:
        file_naam = input("hoe moet de file heten? ")
        opslaan(file_naam)
        
je_naam = input("wat is je naam? ")
start()
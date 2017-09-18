### Sudoku
from pprint import *
from copy import *

# Z = [[6,2,"_","_",9,"_",7,"_",5],[4,"_","_","_",8,"_",6,"_","_"],["_",9,1,"_",5,"_",4,"_","_"],["_","_",3,"_","_",5,2,7,"_"],["_",8,6,3,"_",2,"_","_","_"],["_","_",7,"_",1,"_","_",8,"_"],[8,7,"_","_","_","_","_","_",1],["_","_","_",9,"_",7,"_","_",2],[3,5,2,"_","_","_","_","_","_"]]

### Funktionaler Teil:

def spalten(Z): # Erstellt eine Liste der Spalten
    S = [[Z[j][i] for j in range(9)] for i in range(9)]
    return S

def bloecke(Z): # Erstellt ein Dicionary der Blocke
    K11 = [Z[i][j] for i in range(0,3) for j in range(0,3)]
    K12 = [Z[i][j] for i in range(0,3) for j in range(3,6)]
    K13 = [Z[i][j] for i in range(0,3) for j in range(6,9)]
    K21 = [Z[i][j] for i in range(3,6) for j in range(0,3)]
    K22 = [Z[i][j] for i in range(3,6) for j in range(3,6)]
    K23 = [Z[i][j] for i in range(3,6) for j in range(6,9)]
    K31 = [Z[i][j] for i in range(6,9) for j in range(0,3)]
    K32 = [Z[i][j] for i in range(6,9) for j in range(3,6)]
    K33 = [Z[i][j] for i in range(6,9) for j in range(6,9)]
    KD = {(1,1):K11, (1,2):K12, (1,3):K13, (2,1):K21, (2,2):K22, (2,3):K23, (3,1):K31, (3,2):K32, (3,3):K33}
    return (KD)

def loeserhelp(Z):  # Gibt den nechsten Eintrag an, den der Loeser einfugt.
    KD = bloecke(Z)
    S = spalten(Z)
    ZC = Z.copy()
    i=0
    while i<9:
        j=0
        while j<9:
            if ZC[i][j]!="_":
                j+=1
            else:
                h = []
                for k in range(1,10):
                    if k not in ZC[i] and k not in S[j] and k not in KD[((i//3)+1,(j//3)+1)]:
                        h.append(k)
                if len(h)==1:
                    ZC[i][j] = h[0]
                    S[j][i] = h[0]
                    KD[((i//3)+1,(j//3)+1)].append(h[0])
                    i=100
                    j=100
                else: j+=1
        i+=1
    return(ZC)

def loeser(Z): # Loest leichte Sudoku
    KD = bloecke(Z)
    S = spalten(Z)
    ZC = Z.copy()
    count = 1
    for i in range(9):
        for j in range(9):
            if ZC[i][j]!="_":
                continue
            else:
                h = []
                for k in range(1,10):
                    if k not in ZC[i] and k not in S[j] and k not in KD[((i//3)+1,(j//3)+1)]:
                        h.append(k)
                if len(h)==1:
                    ZC[i][j] = h[0]
                    S[j][i] = h[0]
                    KD[((i//3)+1,(j//3)+1)].append(h[0])
                    count+=1
                    loeser(ZC)
    return(ZC)


def sudokuliste(dateiname): # Erstellt aus einer Datei ein Sudoku als Liste
    sudoku = open(dateiname,"r")
    Z = []
    while True:
        zeile = sudoku.readline()
        zeile2= zeile.rstrip()
        Z.append(zeile2.split("|"))
        if not zeile:
            break
    del Z[9]
    for i in range(9):
        for j in range(9):
            for k in range(1,10):
                if str(k) in str(Z[i][j]):
                    Z[i][j] = k
    sudoku.close()
    return(Z)

def ausgabe(Z): # Gibt ein Sudoku in Listenformat als Sudoku aus, dass sich in eine Datei speichern lasst
    print(Z[0][0],Z[0][1],Z[0][2],Z[0][3],Z[0][4],Z[0][5],Z[0][6],Z[0][7],Z[0][8],sep="|",end="\n")
    print(Z[1][0],Z[1][1],Z[1][2],Z[1][3],Z[1][4],Z[1][5],Z[1][6],Z[1][7],Z[1][8],sep="|",end="\n")
    print(Z[2][0],Z[2][1],Z[2][2],Z[2][3],Z[2][4],Z[2][5],Z[2][6],Z[2][7],Z[2][8],sep="|",end="\n")
    print(Z[3][0],Z[3][1],Z[3][2],Z[3][3],Z[3][4],Z[3][5],Z[3][6],Z[3][7],Z[3][8],sep="|",end="\n")
    print(Z[4][0],Z[4][1],Z[4][2],Z[4][3],Z[4][4],Z[4][5],Z[4][6],Z[4][7],Z[4][8],sep="|",end="\n")
    print(Z[5][0],Z[5][1],Z[5][2],Z[5][3],Z[5][4],Z[5][5],Z[5][6],Z[5][7],Z[5][8],sep="|",end="\n")
    print(Z[6][0],Z[6][1],Z[6][2],Z[6][3],Z[6][4],Z[6][5],Z[6][6],Z[6][7],Z[6][8],sep="|",end="\n")
    print(Z[7][0],Z[7][1],Z[7][2],Z[7][3],Z[7][4],Z[7][5],Z[7][6],Z[7][7],Z[7][8],sep="|",end="\n")
    print(Z[8][0],Z[8][1],Z[8][2],Z[8][3],Z[8][4],Z[8][5],Z[8][6],Z[8][7],Z[8][8],sep="|",end="\n")


### Interaktiver Teil:
erf = 123
while erf == 123:   # Existiert die eingebene Datei
    try:
        eingabe = input("Öffne das Sudoku aus folgender Datei:")
        k = sudokuliste(eingabe)
        erf = 234
    except FileNotFoundError:
        print("Die angegebene Datei existiert nicht.")
        erf = 123
ausgabe(sudokuliste(eingabe))
NA = sudokuliste(eingabe) #Das ursprungliche Sudoku
Z = sudokuliste(eingabe)

option = input("Tippe 1, um das Sudoku selber zu lösen oder 2, um das Sudoku lösen zu lassen.")
f=123
while f==123:
    if option=="1" or option=="2":
        f=234
    else:
        option= input("Deine Eingabe muss 1 oder 2 sein.")
        f=123
if option=="1":
    helf = 123
    while helf==123:
        hilfe = input("Falls du Hilfe brauchst gebe Help ein. Sonst weiter mit Enter:")
        if hilfe !="Help":
            k = 0
            while k < 9:
                test = 0
                if "_" in Z[k]: # testet ob die k-te Zeile komplett ist.
                    test += 111
                if test > 100:  # falls die k-te Zeile noch Luecken hat
                    print("Welchen Eintrag willst du einfügen?")
                    z=0
                    while z == 0: # Testet ob die Eingabe für Zeile sinnvoll ist.
                        eingabe = input("Zeile:")
                        z = 10
                        y = 11
                        try:
                            zeile = int(eingabe)
                        except:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            y = 22
                        if y == 11 and int(eingabe)<1:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            zeile = int(eingabe)
                        elif y == 11 and int(eingabe)>9:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            zeile = int(eingabe)
                    z=0
                    while z == 0: # Testet ob die Eingabe für Spalte sinnvoll ist.
                        eingabe = input("Spalte:")
                        z = 10
                        y = 11
                        try:
                            spalte = int(eingabe)
                        except:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            y = 22
                        if y == 11 and int(eingabe)<1:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            spalte = int(eingabe)
                        elif y == 11 and int(eingabe)>9:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            spalte = int(eingabe)
                    z=0
                    while z == 0: # Testet, ob du Eingabe für Wert sinnvoll ist.
                        eingabe = input("Wert:")
                        z = 10
                        y = 11
                        try:
                            wert = int(eingabe)
                        except:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            y = 22
                        if y == 11 and int(eingabe)<1:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            wert = int(eingabe)
                        elif y == 11 and int(eingabe)>9:
                            print("Deine Eingabe muss eine ganze Zahl zwischen 1 und 9 sein.")
                            z = 0
                            wert = int(eingabe)
                    if NA[zeile-1][spalte-1] !="_": # Damit das Sudoku nicht komplett veraenderbar ist.
                        print("Diesen Eintrag darfst du nicht verändern.")
                        k = 0
                    elif wert not in Z[zeile-1] and wert not in spalten(Z)[spalte-1] and wert not in bloecke(Z)[(((zeile-1)//3)+1,((spalte-1)//3)+1)]:
                        Z[zeile-1][spalte-1] = wert
                        ausgabe(Z) # Falls die Eingabe sinnvoll ist und der Wert in Spalte,Zeile,Block noch nicht vorkommt, wird der Wert geaendert.
                        k = 100     #Zurueck zur Hilfefunktion
                        test = 111
                    else:
                        print("Der Wert",wert,"passt hier nicht rein.",sep=" ") # Falls der Wert schonmal in Spalte,Zeile oder Block vorkommt, wird eine neue Eingabe verlangt.
                        k = 0
                if test == 0:
                    k +=1
            if test == 0: # falls das Sudoku vollstaendig ausgefuellt ist.
                i=1
                while i<=9: # testet, ob jede Zahl pro Zeile, Spalte und Block genau einmal vorkommt.
                    j=0
                    while j<9:
                        if  Z[j].count(i)>1:
                            print("In deine Lösung hat sich ein Fehler eingeschlichen.")
                            i=100
                            j=100
                            helf = 234
                        elif spalten(Z)[j].count(i)>1:
                            print("In deine Lösung hat sich ein Fehler eingeschlichen.")
                            i=100
                            j=100
                            helf = 234
                        elif True:                
                            for r in range(3):
                                if bloecke(Z)[((j//3)+1,r+1)].count(i)>1:
                                    print("In deine Lösung hat sich ein Fehler eingeschlichen.")
                                    i=100
                                    j=100
                                    helf = 234
                                    break
                                else: j +=1
                        else: j+=1
                    i+=1
                if i==10: # falls das Sudoku vollständig und richtig geloest wurde.
                    print("Gratulation! Du hast das Sudoku richtig gelöst.")
                    helf = 234    #Die Hilfefunktion wird nicht mehr benoetigt.
        if hilfe=="Help":
            Z3 = deepcopy(Z)
            if Z3 == loeserhelp(Z):
                print("Dieses Sudoku ist zu schwer für mich.")
            else:
                ausgabe(Z)

if option=="2":
    ausgabe(loeser(sudokuliste(eingabe)))
    Z = loeser(sudokuliste(eingabe))
    i=1
    while i<=9: # testet, ob jede Zahl pro Zeile, Spalte und Block genau einmal vorkommt.
        j=0
        while j<9:
            if  Z[j].count(i)>1:
                print("Die {0} kommt in der {1}. Zeile mehrfach vor.".format(i,j))
                i=100
                j=100
            elif spalten(Z)[j].count(i)>1:
                print("Die {0} kommt in der {1}. Spalte mehrfach vor.".format(i,j))
                i=100
                j=100
            elif True:                
                for r in range(3):
                    if bloecke(Z)[((j//3)+1,r+1)].count(i)>1:
                        print("Die {0} kommt im  Block {1} mehrfach vor.".format(i,((j//3)+1,r+1)))
                        i=100
                        j=100
                        break
                    else: j +=1
            else: j+=1
        i+=1
    for k in range(9):  #kontrolliert, ob das Sudoku vollstaendig geloest wurde.
        if "_" in Z[k]:
            print("Das Sudoku konnte nicht vollstädig gelöst werden.")
            break



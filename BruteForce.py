import sys
sys.setrecursionlimit(10000)
import copy
Z = [[6,2,"_","_",9,"_",7,"_",5],[4,"_","_","_",8,"_",6,"_","_"],["_",9,1,"_",5,"_",4,"_","_"],["_","_",3,"_","_",5,2,7,"_"],["_",8,6,3,"_",2,"_","_","_"],["_","_",7,"_",1,"_","_",8,"_"],[8,7,"_","_","_","_","_","_",1],["_","_","_",9,"_",7,"_","_",2],[3,5,2,"_","_","_","_","_","_"]]

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




def spalten(Z): # Erstellt eine Liste der Spalten
    S = [[Z[j][i] for j in range(9)] for i in range(9)]
    return S

def bloecke(Z): # Erstellt ein Dicionary der Blöcke als Listen
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
                    loeser(ZC)
    return(ZC)

def entrees(Z):
    KD = bloecke(Z)
    S = spalten(Z)
    ZC = Z.copy()
    matrix = [
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]]
             ]
    for i in range(9):
        for j in range(9):
            if ZC[i][j]!="_":
                continue
            else:
                h = []
                for k in range(1,10):
                    if k not in ZC[i] and k not in S[j] and k not in KD[((i//3)+1,(j//3)+1)]:
                        h.append(k)
                matrix[i][j] = h
    return matrix


def zuordnung1(m,n,Z): #soll jeder Zahl von 1 bis 9 die möglichen Felder im Block (m,n) des Sudokus Z zuordnen
    i = 1
    L = []
    while i < 10:
        if i in bloecke(Z)[m,n]:
            i+=1
        else:
            L.append(i)
            i+=1
    Dict = {}
    for k in L:
        options=[]
        j = 0
        while j<9:
            Zeile = Z[3*(m-1)+(j//3)]
            Spalte = spalten(Z)[3*(n-1)+(j%3)]
            if bloecke(Z)[m,n][j] is not "_":
                j+=1
            elif k in Zeile or k in Spalte:
                j+=1
            else:
                options.append(j)
                j+=1
        Dict2 = {(k):options}
        Dict.update(Dict2)
    return(Dict)




def loeserneu(Z):
    Bloecke = bloecke(Z)
    Spalten = spalten (Z)
    test = 0
    for k in range(9):
        if "_" in Z[k]:
            test+=1
    while test!=0:
        for m in range(3):
            for n in range(3):
                for key in zuordnung1(n+1,m+1,Z):
                    if len(zuordnung1(n+1,m+1,Z)[key])==1:
                        j = zuordnung1(n+1,m+1,Z)[key][0]
                        Z[3*n+(j//3)][3*m+(j%3)]=key
                    else:
                        continue
        test=0
    return Z

def eintraege(Z):
    values=[]
    for k in range(9):
        values.extend(Z[k])
    return values

def superloeser(Z): # this function is able to solve not only easy or normal Sudokus
    while "_" in eintraege(Z):
        Y = loeserneu(Z)
        Y = loeser(Y)
        if Y!=Z:
            Z = Y
        else:
            return Z
    return Z

def control(Z):
    E = entrees(Z)
    for i in range(9):
        for j in range(9):
            if Z[i][j]=="_":
                if E[i][j]==[]:
                    return False
                else: continue
            else: continue
    return True

def BruteForce(Z,L=[]):
    # Z is the Sudoku as a list
    # L contains the previous Sudoku, the indice i and j of the last step
    ### and the number which was entered in L[0][i][j]
    if "_" in eintraege(Z):
        if control(Z)==True:
            l = 1
            while l < 10:
                r=0
                while r <9:
                    s=0
                    while s<9:
                        if len(entrees(Z)[r][s]) == l:
                            New = copy.deepcopy(Z)
                            i = copy.deepcopy(r)
                            j = copy.deepcopy(s)
                            L.append([New,i,j,entrees(Z)[i][j],entrees(Z)[i][j][0]])
                            Z[i][j] = entrees(Z)[i][j][0]
                            r=10
                            s=10
                            l=10
                        else: s+=1
                    r+=1
                l+=1
         # Hier verwirft der Algorithmus die letzte Eintragung
         # Er muss zur letzten Auswahl zurückkehren
         # Dabei darf er keine Informationen verlieren
        else:
            while len(L[-1][3]) == 1:
                L.pop(-1)
            i = L[-1][1]
            j = L[-1][2]
            Z = L[-1][0]
            L[-1][3].remove(L[-1][4])
            Z[i][j] = "_"
            Z[i][j] = L[-1][3][0]
            L[-1][0] = Z
        return BruteForce(Z,L)
    else:
        return Z

ausgabe(BruteForce(sudokuliste("seventeen")))

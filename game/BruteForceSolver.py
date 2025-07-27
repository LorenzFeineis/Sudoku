import sys
sys.setrecursionlimit(10000)
import copy
from common import sudokuliste, ausgabe, spalten, bloecke


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


def eintraege(Z):
    values=[]
    for k in range(9):
        values.extend(Z[k])
    return values


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

ausgabe(BruteForce(sudokuliste("./data/Leer")))

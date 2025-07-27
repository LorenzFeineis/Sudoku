### Sudoku
from common import bloecke, spalten

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



from common import bloecke, spalten, ausgabe, sudokuliste
from SimpleSolver import loeser


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
            if bloecke(Z)[m,n][j] != "_":
                j+=1
            elif k in Zeile or k in Spalte:
                j+=1
            else:
                options.append(j)
                j+=1
        Dict2 = {(k):options}
        Dict.update(Dict2)
    return(Dict)


def advancedSolver(Z):
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

def combined_solver(Z): # this function is able to solve not only easy or normal Sudokus
    while "_" in eintraege(Z):
        Z = advancedSolver(Z)
        Z = loeser(Z)
    return Z

ausgabe(combined_solver(sudokuliste("data/SehrSchwer.txt")))




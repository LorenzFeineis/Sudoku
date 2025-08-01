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

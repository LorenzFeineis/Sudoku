### Sudoku
import pprint
from pprint import *

Z = [[6,2,"_","_",9,"_",7,"_",5],[4,"_","_","_",8,"_",6,"_","_"],["_",9,1,"_",5,"_",4,"_","_"],["_","_",3,"_","_",5,2,7,"_"],["_",8,6,3,"_",2,"_","_","_"],["_","_",7,"_",1,"_","_",8,"_"],[8,7,"_","_","_","_","_","_",1],["_","_","_",9,"_",7,"_","_",2],[3,5,2,"_","_","_","_","_","_"]]

def Löser(Z):
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
    S = [[Z[j][i] for j in range(9)] for i in range(9)]
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
                    Löser(ZC)

    return(ZC,count)
            
pprint(Löser(Z))

sudoku = open("Sudoku.txt","r")
Z2=[]
while True:
    zeile = sudoku.readline()
    zeile2= zeile.rstrip()
    Z2.append(zeile2.split("|"))
    if not zeile:
        break
del Z2[9]
for i in range(9):
    for j in range(9):
        for k in range(1,10):
            if str(k) in str(Z2[i][j]):
                Z2[i][j] = k

pprint(Löser(Z2))

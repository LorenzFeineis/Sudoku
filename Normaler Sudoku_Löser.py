import pprint
from pprint import pprint
Z = [[6,2,"_","_",9,"_",7,"_",5],[4,"_","_","_",8,"_",6,"_","_"],["_",9,1,"_",5,"_",4,"_","_"],["_","_",3,"_","_",5,2,7,"_"],["_",8,6,3,"_",2,"_","_","_"],["_","_",7,"_",1,"_","_",8,"_"],[8,7,"_","_","_","_","_","_",1],["_","_","_",9,"_",7,"_","_",2],[3,5,2,"_","_","_","_","_","_"]]
M = [1,2,3,4,5,6,7,8,9]
ZM = [[M for j in range(9)] for i in range(9)]

def Löser(Z):
    M = [1,2,3,4,5,6,7,8,9]
    ZM = [[M for j in range(9)] for i in range(9)]
    K11 = [[Z[i][j] for i in range(0,3)] for j in range(0,3)] # 3x3 Matrix
    K12 = [[Z[i][j] for i in range(0,3)] for j in range(3,6)]
    K13 = [[Z[i][j] for i in range(0,3)] for j in range(6,9)]
    K21 = [[Z[i][j] for i in range(3,6)] for j in range(0,3)]
    K22 = [[Z[i][j] for i in range(3,6)] for j in range(3,6)]
    K23 = [[Z[i][j] for i in range(3,6)] for j in range(6,9)]
    K31 = [[Z[i][j] for i in range(6,9)] for j in range(0,3)]
    K32 = [[Z[i][j] for i in range(6,9)] for j in range(3,6)]
    K33 = [[Z[i][j] for i in range(6,9)] for j in range(6,9)]
    KD = {(1,1):K11, (1,2):K12, (1,3):K13, (2,1):K21, (2,2):K22, (2,3):K23, (3,1):K31, (3,2):K32, (3,3):K33}
    S = [[Z[j][i] for j in range(9)] for i in range(9)] # 9x9 Matrix
    ZC = Z.copy()
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,10):
                if k not in KD[(i,j)]:
                    z1 = []
                    s1 = []
                    for z in range(3):
                        if k in ZC[3*(i-1)+z]:
                            z1.append(z)
                    for s in range(3):
                        if k in S[3*(j-1)+s]:
                            s1.append(s)
                    
                else: pass
    return z

print(Löser(Z))
         




















#    for i in range(9):
#        for j in range(9):
#            if Z[i][j]=="_":
#                for k in range(1,10):
#                    if k in ZM[i][j]:
#                        if k in Z[i] or k in S[j] or k in KD[((i//3)+1,(j//3)+1)]:
#                            del ZM[i][j][ZM[i][j].index(k)]
#                if len(ZM[i][j])==1:
#                    ZC[i][j]=ZM[i][j][0]
#                    S[j][i]=ZM[i][j][0]
#                    KD[((i//3)+1,(j//3)+1)].append(ZM[i][j][0])
#                    Löser(ZC)
#                else: continue
#            else: continue
#        else: continue
#    return(ZC)

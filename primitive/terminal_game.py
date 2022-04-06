#!/usr/bin/env python3
"""
A terminal game to play Sudoku.

Load or solve a sudoku manually or use help from an implemented solver.
"""
from Loeser import *

from pprint import *
from copy import *

def main():
    '''Start game in the interactive shell.'''
    while True:   # Existiert die eingebene Datei
        try:
            eingabe = input("Öffne das Sudoku aus folgender Datei:")
            k = sudokuliste(eingabe)
            break
        except FileNotFoundError:
            print("Die angegebene Datei existiert nicht.")
    ausgabe(sudokuliste(eingabe))
    NA = sudokuliste(eingabe) #Das ursprungliche Sudoku
    Z = sudokuliste(eingabe)

    option = input("Tippe 1, um das Sudoku selber zu lösen oder 2, um das Sudoku lösen zu lassen.")
    while True:
        if option=="1" or option=="2":
            break
        else:
            option= input("Deine Eingabe muss 1 oder 2 sein.")
    if option=="1":
        while True:
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
                                break
                            elif spalten(Z)[j].count(i)>1:
                                print("In deine Lösung hat sich ein Fehler eingeschlichen.")
                                i=100
                                j=100
                                break
                            elif True:
                                for r in range(3):
                                    if bloecke(Z)[((j//3)+1,r+1)].count(i)>1:
                                        print("In deine Lösung hat sich ein Fehler eingeschlichen.")
                                        i=100
                                        j=100
                                        break
                                    else: j +=1
                            else: j+=1
                        i+=1
                    if i==10: # falls das Sudoku vollständig und richtig geloest wurde.
                        print("Gratulation! Du hast das Sudoku richtig gelöst.")
                        break    #Die Hilfefunktion wird nicht mehr benoetigt.
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

if __name__ == '__main__':
    main()

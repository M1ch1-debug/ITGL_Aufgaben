# Aufgabe 1:
# Schreiben Sie ein Python-Programm, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnen und ausgeben
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotienten kleinere der beiden Zahlen durch die größere Zahl berechnen und ausgeben (inkl. Nachkommastellen)

#1
print("Hallo lieber Benutzer!")

#2
erste_zahl_string = input("Eingabe einer ersten Zahl:")
erste_zahl = float(erste_zahl_string)
print("Die Eingabe für die erste Zahl lautete:", erste_zahl)

#3
zweite_zahl_string = input("Eingabe einer zweiten Zahl:")
zweite_zahl = float(zweite_zahl_string)
print("Die Eingabe für die zweite Zahl lautete:", zweite_zahl)

#4
print("Summe:",erste_zahl+zweite_zahl)

#5
if  erste_zahl >= zweite_zahl :
    print("Differenz:",erste_zahl-zweite_zahl)
else:
    print("Differenz:",zweite_zahl-erste_zahl)
#6
print("Produkt:",erste_zahl*zweite_zahl)

#7
if  erste_zahl <= zweite_zahl :
    print("Ouotient:",erste_zahl/zweite_zahl)
else:
    print("Quotient:",zweite_zahl/erste_zahl)
    
    
obererTerm = 1
pi_4 = 0
zahl1 = input("Geben Sie die Anzahl der Iterationen ein")
zahl1 = int (zahl1)
for k in range(0,zahl1) :
   pi_4 += obererTerm / (2*k+1)
   obererTerm = obererTerm * (-1)
print(pi_4*4)



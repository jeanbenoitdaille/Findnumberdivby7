resultat = []
     
for i in range(0, 1001):
        if (i % 7 == 0) and (i % 3 != 0):
            resultat.append(i)
     
print(resultat)
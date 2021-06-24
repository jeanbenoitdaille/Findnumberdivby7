# Findnumberdivby7
Trouver les nombres divisibles par 7 mais pas multiples de 3 
Encore un exercice pour vous faire pratiquer le modulo.

Dans cet exercice, on cherche les nombres divisibles par 7, donc dont le reste de la division par 7 donne 0.
Nous cherchons également à savoir si ces même nombres ne sont pas des multiples de 3 (donc dont le reste de la division n'est pas égal à 0).

Nous allons donc encore une fois utiliser l'opérateur modulo pour vérifier ces deux conditions.

Tout d'abord, nous créons une liste "resultat" qui va contenir tous les nombres qui confirment les deux conditions.

On par donc dans une boucle sur une liste de nombres allant de 0 à 1000 :

    for i in range(0, 1001):

Ensuite, on teste les deux conditions : on utilise l'opérateur 'and' pour vérifier que les deux conditions soient vraies.
Si une seule des deux conditions n'est pas respectée, le nombre ne sera pas ajouté. Les deux conditions testées sont :

    (i % 7 == 0)
    (i % 3 != 0)

La première testant si le nombre est divisible par 7 et la deuxième testant si le nombre n'est pas multiple de 3.

Si ces deux conditions sont vérifiées, on ajoute le nombre dans la liste :

    resultat.append(i)

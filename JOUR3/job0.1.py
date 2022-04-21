# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de
# fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
# ni ... boucle. Seulement de la récursivité.

n = int(input())

def puissance(x, n):
    if (n==0):
        return(1)

    resultat = x * puissance(x, n - 1)
    return (resultat)

print(puissance(2, n))


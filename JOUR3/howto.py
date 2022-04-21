# 2^1 = 2 * 2^0 mais du coup ça rentre dans le if (ligne 9) et ça donne : 2 * 1
# 2^2 = 2 * 2^1 donc 2*2
# 2^3 = 2 * 2^2 
# 2^4 = 2 * 2^3
# 2^5 = 2 * 2^4
# x^n = x * x^n-1

def puissance(x, n):
    if (n==0):
        return(1)

    resultat = x * puissance(x, n - 1)
    return (resultat)

print(puissance(2, 4))
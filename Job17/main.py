# Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les multiples de
# trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
# les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".


i = range(1, 100)

for l in i:
    if ((l%3==0) or (l%5==0)):
        if ((l%3==0) and (l%5!=0)):
            print("Fizz")
        if ((l%5==0) and (l%3!=0)):
            print("Buzz")
        if ((l%3==0) and (l%5==0)):
            print("FizzBuzz")
    else:
        print(l)


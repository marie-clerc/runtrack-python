# Créez un programme qui demande 5 fois à l’utilisateur de renseigner un nombre entier.
# Stockez ces nombres entiers dans une liste puis triez-les par ordre croissant avant de
# les afficher, dans l’ordre, dans le terminal.


num1 = int(input("1x entrer un nombre entier: "))
num2 = int(input("2x entrer un nombre entier: "))
num3 = int(input("3x entrer un nombre entier: "))
num4 = int(input("4x entrer un nombre entier: "))
num5 = int(input("5x entrer un nombre entier: "))
list = [num1, num2, num3,num4,num5]
croissant = sorted(list, reverse=False)
print(croissant)
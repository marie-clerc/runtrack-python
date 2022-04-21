# Créer une classe “Livre” avec comme attribut un “titre” qu’elle reçoit en paramètre à la
# construction et une référence vers une classe “Auteur”. 
# Ajouter une méthode “print” permettant d’afficher dans le terminal le titre du livre. 
# Créer une classe “Auteur” héritant de la classe “Personne” recevant un nom et un prénom en paramètre de construction.
# La classe auteur devra posséder une collection de livres nommée "œuvre" en attribut
# ainsi qu’une méthode “listerOeuvre” affichant dans le terminal la liste des livres écrits
# par l’auteur.


from locale import ABDAY_1


class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Auteur(Personne):
    def __init__(self, nom, prenom, oeuvre):
        Personne.__init__(self, nom, prenom)
        self.oeuvre = oeuvre

    def listerOeuvre(self):
        oeuvres = []
        while True: 
            oeuvres.append(Livre.printBook)
            next_livre =  input("un autre titre de livre ? (yes/no)")
            if next_livre == "no":
                break
# Ajouter à la classe Auteur une méthode “ecrireUnLivre” 
# prenant en
# paramètre un titre de livre à écrire et générer une instance 
# de la classe livre avec ce
# titre. Ajouter ce nouveau livre à l’oeuvre de l’auteur  

    # def ecrireUnLivre(self):



class Livre(Auteur):
    def __init__(self, nom, prenom, oeuvre, titre):
        Auteur.__init__(self, nom, prenom, oeuvre)
        self.titre = titre

    def printBook(self):
        print(self.titre)



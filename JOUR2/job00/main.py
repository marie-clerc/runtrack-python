class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.set_nom(nom)
        self.set_prenom(prenom)

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def SePresenter(self):
        print(self.nom, self.prenom)

E1 = Personne("Hermione", "Granger")
E2 = Personne("Katniss", "Everdeen")
E3 = Personne("Newt", "Scamander")


print("Eleve numéro 1 : ")
E1.SePresenter()

print("Eleve numéro 2 : ")
print(E2.get_nom())
print(E2.get_prenom())

print("Eleve numéro 3 : ")
E3.set_nom("Credence")
E3.set_prenom("Barebone")
print(E3.get_nom())
print(E3.get_prenom())
class Vehicule():
	def __init__(self, roue, marque, couleur):
		self.roue = roue
		self.marque = marque
		self.couleur = couleur

	def printmarque(self):
		print(self.marque)

class Camion(Vehicule):
	def __init__(self, roue, marque, couleur, moteur):
		super().__init__(roue, marque, couleur)
		# Vehicule.__init__(self, roue, marque, couleur)
		self.moteur = moteur

	def printmoteur(self):
		print(self.moteur)

V1= Vehicule(4, 'mercedes', 'bleu')
C1= Camion(8, 'Renault', 'rouge', 500)

C1.printmarque()

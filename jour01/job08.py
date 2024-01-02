import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
cercle1.afficherInfos()
cercle2.afficherInfos()

# Affichage de la circonférence, du diamètre et de l'aire pour chaque cercle
print(f"Cercle 1 - Circonférence : {cercle1.circonférence()}, Diamètre : {cercle1.diametre()}, Aire : {cercle1.aire()}")
print(f"Cercle 2 - Circonférence : {cercle2.circonférence()}, Diamètre : {cercle2.diametre()}, Aire : {cercle2.aire()}")
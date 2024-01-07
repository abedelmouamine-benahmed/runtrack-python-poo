class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom
# Instanciation de la classe Animal
mon_animal = Animal()
mon_animal.vieillir()
mon_animal.nommer("Luna")

print(f"L'animal se nomme {mon_animal.prenom} ")

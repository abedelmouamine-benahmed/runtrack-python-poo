# Créer une classe Operation avec un constructeur (méthode qui sera appelée lors de
# l’instance de la classe). Ajouter les attributs “nombre1” et “nombre2” initialisés avec des
# valeurs par défaut. Instancier votre première classe et imprimer l’objet en console.

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
mon_operation = Operation()

# Impression de l'objet en console
print("Valeur de nombre1:", mon_operation.nombre1)
print("Valeur de nombre2:", mon_operation.nombre2)
class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits

    # Assesseurs (getters)
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    # Mutateurs (setters)
    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def set_numero_etudiant(self, nouveau_numero_etudiant):
        self.__numero_etudiant = nouveau_numero_etudiant

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            print(f"{nombre_credits} crédits ajoutés. Total de crédits : {self.__credits}")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

# Instanciation d'un objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(5)
john_doe.add_credits(15)

# Affichage du total de crédits
print(f"Le nb de credits de John Doe est de {john_doe.get_credits()} points")

def __studentEval(self):
    if self.__credits >= 90:
        return "Excellent"
    elif self.__credits >= 80:
        return "Très bien"
    elif self.__credits >= 70:
        return "Bien"
    elif self.__credits >= 60:
        return "Passable"
    else:
        return "Insuffisant"

# Méthode pour afficher les informations de l'étudiant
def studentInfo(self):
    print(f"Informations de l'étudiant {self.__nom} {self.__prenom} :")
    print(f"Identifiant : {self.__numero_etudiant}")
    print(f"Total de crédits : {self.__credits}")
    print(f"Niveau : {self.__level}")


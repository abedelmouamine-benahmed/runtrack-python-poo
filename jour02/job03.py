class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible
        # Méthode pour emprunter le livre
    def emprunter(self):
        if self.__disponible:
            print("Le livre a été emprunté.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.__disponible:
            print("Le livre a été rendu.")
            self.__disponible = True
        else:
            print("Le livre est déjà disponible.")

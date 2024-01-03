class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvelle_valeur):
        self.__en_marche = nouvelle_valeur

    def set_reservoir(self, nouvelle_valeur):
        self.__reservoir = nouvelle_valeur

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir > 5

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer. Niveau de réservoir trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'est arrêtée.")

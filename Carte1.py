class Carte:
        def __init__(self, val, coul):
            self.valeur = val
            self.couleur = coul
        def affiche(self):
                print(self.valeur, "de", self.couleur)

class Carte:
  def __init__(self, val, coul):
    if val < 2 or val > 14:
        print ("Erreur : La vleur d'une carte est comprise entre 2 et 14")
        exit(1)
    if coul < 0 or coul > 3:
        print("Erreur : Le Code couleur d'une carte est compris entre 0 et 3")
        exit(1)
    self.valeur = val
    self.couleur = coul

    def affiche(self):
        affiche_valeur = None
        affiche_couleur = None

        if self.valeur <= 10:
            affiche_valeur = self.valeur
        elif self.valeur == 11:
            affiche_valeur = "Valet"
        elif self.valeur == 12:
            affiche_valeur = "Dame"
        elif self.valeur == 13:
            affiche_valeur = "Roi"
        else:
            affiche_valeur = "As"

        if sel.couleur == 0:
            affiche_couleur = "Coeur"
        elif sel.couleur == 1:
            affiche_couleur = "Carreau"
        elif affiche_couleur == 2:
            affiche_couleur = "Trèfle"
        else:
            affiche_couleur = "Pique"

        print("Le", affiche_valeur, "de", affiche_couleur)

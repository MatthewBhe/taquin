from math import *
from random import *

class Taquin():
    """
    Classe Taquin : permet de définir un objet pour le jeu du taquin
    Constructeur :
        - __init__(self, txt) : gestion de l'affichage, du déplacement et de la victoire du taquin
    Attributs :
        - contenu : liste représentant le taquin
        - etat : chaîne de caractères représentant le taquin
        - nbcol : nombre de colonnes
        - nblig : nombre de lignes
    Methodes :
        - __str__(self) : permet un affichage conventionnel en carré
        - rangezero(self) : permet de donner la position du zero, donc de la case à déplacer
        - inverser(self,rang1,rang2) : permet d´inverser la position de 2 valeurs dans la liste. Utile pour les déplacements
        - haut(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
        - bas(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
        - gauche(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
        - droite(self) : vérifie si le déplacement est faisable et réalise l'inversion des positions
        - melanger(self,profondeur) : réalise une série de mouvement aléatoire à partir d'une position initiale pour mélanger le taquin
        - gagnant(self) : vérifie si la position actuelle est la position gagnante, utilise la classe Etat
    """
    # constructeur
    def __init__(self, txt):
        # la liste qui représente la taquin en mémoire
        liste = []
        for i in txt:
            liste.append(i)
        self.contenu = liste

        # gestion de la taille si on veut travailler sur un taquin plus grand mais toujours carré
        self.nbcol = int(sqrt(len(liste)))
        self.nblig = int(sqrt(len(liste)))
        # stocke l'état du taquin sous la forme d'une chaîne de caractères
        self.etat = txt

    # affichage
    def __str__(self):
        affichage = ''
        for i in range (0,self.nbcol):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        for i in range (self.nbcol,self.nbcol*2):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        for i in range (self.nbcol*2,self.nbcol*3):
            affichage = affichage + str(self.contenu[i]) + ' '
        affichage = affichage + '\n'
        return(affichage)

    # méthode qui permet de mettre à jour l'état du taquin à partir de son contenu (liste)
    def majetat(self):
        self.etat = ''
        for i in self.contenu:
            self.etat = self.etat + str(i)

    # méthode qui permet de connaître la position de la case vide (zéro)
    def rangzero(self):
        return(self.contenu.index('0'))

    # méthode qui permet d'échanger la position de deux éléments de la liste "contenu", et modifie l'attribut etat en conséquence
    def echanger(self,rang1, rang2):
        tmp1 = self.contenu[rang1]
        tmp2 = self.contenu[rang2]
        self.contenu[rang1] = tmp2
        self.contenu[rang2] = tmp1
        self.majetat()

    # les quatre méthodes suivantes permettent de modifier le taquin selon le mouvement souhaité d'une case
    # les mouvements se font par rapport à la case vide : on échange la position de la case vide avec la case ciblée
    def haut(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang > 2:
            self.echanger(rang, rang-3)

    def bas(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang < 6:
            self.echanger(rang, rang+3)

    def gauche(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang != 0 and rang != 3 and rang != 6:
            self.echanger(rang, rang-1)

    def droite(self):
        rang = self.rangzero()
        # vérifie si le déplacement est faisable avant l'échange
        if rang != 2 and rang != 5 and rang != 8:
            self.echanger(rang, rang+1)

    # méthode qui effectue une série de mouvements choisis aléatoirement afin de mélanger le taquin
    def melanger(self, nbdefois):
        while (self.estGagnant() != False):
            for i in range (0, nbdefois):
                move = randint(1,4)
                if move == 1:
                    self.haut()
                elif move == 2:
                    self.bas()
                elif move == 3:
                    self.droite()
                elif move == 4:
                    self.gauche()


    # méthode qui permet de vérifier si l'état actuel est gagnant
    def estGagnant(self):
        averif = self.etat
        if averif == '012345678':
            return True
        else:
            return False

    # méthode qui renvoie la liste des états suivants du taquin par rapport à son état actuel
    def suivants(self):
        # automate qui prend un etat en entrée et renvoie une chaine avec l'ensemble de setats accessibles depuis l'etat d'entrée
        position=self.rangzero()
        eH = ''
        eB = ''
        eD = ''
        eG = ''
        rendu=[]

        if position == 0:
            eH = ''
            eB = self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = ''

        if position == 1:
            eH = ''
            eB = self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = self.etat[1]+self.etat[0]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]

        if position == 2:
            eH = ''
            eB = self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
            eD = ''
            eG = self.etat[0]+self.etat[2]+self.etat[1]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]

        if position == 3:
            eH = self.etat[3]+self.etat[1]+self.etat[2]+self.etat[0]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = ''

        if position == 4:
            eH = self.etat[0]+self.etat[4]+self.etat[2]+self.etat[3]+self.etat[1]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[4]+self.etat[3]+self.etat[5]+self.etat[6]+self.etat[7]+self.etat[8]

        if position == 5:
            eH = self.etat[0]+self.etat[1]+self.etat[5]+self.etat[3]+self.etat[4]+self.etat[2]+self.etat[6]+self.etat[7]+self.etat[8]
            eB = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
            eD = ''
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[5]+self.etat[4]+self.etat[6]+self.etat[7]+self.etat[8]

        if position == 6:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[6]+self.etat[4]+self.etat[5]+self.etat[3]+self.etat[7]+self.etat[8]
            eB = ''
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]
            eG = ''

        if position == 7:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[7]+self.etat[5]+self.etat[6]+self.etat[4]+self.etat[8]
            eB = ''
            eD = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[7]+self.etat[6]+self.etat[8]

        if position == 8:
            eH = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[8]+self.etat[6]+self.etat[7]+self.etat[5]
            eB = ''
            eD = ''
            eG = self.etat[0]+self.etat[1]+self.etat[2]+self.etat[3]+self.etat[4]+self.etat[5]+self.etat[6]+self.etat[8]+self.etat[7]

        if eH != '':
            rendu.append(eH)
        if eB != '':
            rendu.append(eB)
        if eG != '':
            rendu.append(eG)
        if eD != '':
            rendu.append(eD)
        return(rendu) 
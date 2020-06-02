# -*- coding: utf-8 -*-
from backend import *

equipe = 0

print('Voici la liste des championnats avec leur id')
for row in liste_championnat():
    print(row)
print('------------------')

    
print('Voici la liste des équipes de la Ligue 1')
for row in liste_equipe(1):
    print(row)
print('------------------')

print('Voici la liste des buteurs de la Ligue 1')
for row in liste_buteur(1):
    print(row)
print('------------------')


print('Voici le nombre de but d\'un joueur ici K. Mbappé')
print(nbr_but_joueur('K. Mbappé'))
print('------------------')

print('Voici le nombre point d\'une équipe')
print(nbr_point(equipe))
print('------------------')

print('Voici la différence de but d\'une équipe')
print(dif_but(equipe))
print('------------------')

print('Voici le nombre de clean sheet (aucun but encaissé) d\'une équipe')
print(clean_sheet(equipe))
print('------------------')

print('Voici les derniers match d\'une équipe')
print(derniersmatchs(equipe))
print('------------------')

print('Voici le nombre de match sans défaite d\'une équipe')
print(no_loose(equipe))
print('------------------')

print('Voici le nombre de match avec plus de 2 buts d\'une équipe')
print(plus_de_deux_but(equipe))
print('------------------')
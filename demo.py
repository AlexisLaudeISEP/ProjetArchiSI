# -*- coding: utf-8 -*-
from backend import *


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
print(nbr_point(141))
print('------------------')

print('Voici la différence de but d\'une équipe')
print(dif_but(141))
print('------------------')

print('Voici le nombre de clean sheet (aucun but encaissé) d\'une équipe')
print(clean_sheet(141))
print('------------------')

print('Voici les derniers match d\'une équipe')
print(derniersmatchs(141))
print('------------------')

print('Voici le nombre de match sans défaite d\'une équipe')
print(no_loose(141))
print('------------------')

print('Voici le nombre de match avec plus de 2 buts d\'une équipe')
print(plus_de_deux_but(141))
print('------------------')
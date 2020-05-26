# -*- coding: utf-8 -*-
import mysql.connector
from backend import *
 
conn = mysql.connector.connect(host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
                               user="adminSI", password="mypasswordarchis!", 
                               database="Schema1")
cursor = conn.cursor()

# goal = dif_but_id(1)
# print(goal)
chaine = str(1)
queryButMarque=cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur INNER JOIN Schema1.Joueur ON Schema1.Buteur.idJoueur = Schema1.Joueur.idJoueur WHERE idEquipe = 1")
queryButPrisDom=cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 = 1")
queryButPrisExt=cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = 1")
nbrButMarque = 0
nbrButPrisDom = 0
nbrButPrisExt = 0
for row in queryButMarque:
    nbrButMarque = row[0]
for row in queryButPrisDom:
    nbrButPrisDom = row[0]
for row in queryButPrisExt:
     nbrButPrisExt = row[0]
    
res = (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))
print(res)
     
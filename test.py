# -*- coding: utf-8 -*-
import mysql.connector
from backend import *
 
conn = mysql.connector.connect(host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
                               user="adminSI", password="mypasswordarchis!", 
                               database="Schema1")
cursor = conn.cursor()

print(derniersmatchs(132))



nbrButMarque = 0
nbrButPrisDom = 0
nbrButPrisExt = 0
# cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe = 1")
# for row in cursor:
#     nbrButMarque = row[0]
# cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 = 1")
# for row in cursor:
#     nbrButPrisDom = row[0]
# cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = 1")
# for row in cursor:
#       nbrButPrisExt = row[0]
    
# res = (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))
# print(res)

loose = no_loose(132)
print(loose)
win = no_win(132)
print(win)
print(clean_shit(133))
print(plus_de_deux_but(133))
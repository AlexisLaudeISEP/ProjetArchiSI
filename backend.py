#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:02:48 2020

@author: jullian
"""

import mysql.connector

 
conn = mysql.connector.connect(host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
                               user="adminSI", password="mypasswordarchis!", 
                               database="Schema1")
cursor = conn.cursor()

class Equipe():
    
    def __init__(self,idEquipe,point,dif):
        self.idEquipe=idEquipe
        self.point=point
        self.dif=dif
        
    def creation_equipe():
        cursor.execute("SELECT * FROM Schema1.Equipe")
        for row in cursor:
            Equipe((row[0],0,0))
    

    def nbr_point(equipe):
        NbrVictoire=cursor.execute("SELECT COUNT(*) FROM Schema1.Match WHERE idEquipe1 = "+ equipe.idEquipe + "AND butEquipe1>butEquipe2")
        NbrNul=cursor.execute("SELECT COUNT(*) FROM Schema1.Match WHERE idEquipe1 ="+ equipe.idEquipe +" AND butEquipe1=butEquipe2")
        return (NbrVictoire*3)+ NbrNul
    
    
    def dif_but(equipe):
        nbrButMarque=cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur INNER JOIN Schema1.Joueur ON Schema1.Buteur.idJoueur = Schema1.Joueur.idJoueur WHERE idEquipe ="+equipe.idEquipe)
        nbrButPrisDom=cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 ="+ equipe.idEquipe)
        nbrButPrisExt=cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = "+ equipe.idEquipe)
        return (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))
    
    def but_premiere_mitemps(equipe):
        nbrButMarque=cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur INNER JOIN Schema1.Joueur ON Schema1.Buteur.idJoueur = Schema1.Joueur.idJoueur WHERE idEquipe ="+equipe.idEquipe)
        nbrButPremiere=cursor.execute("")
        
        
    

class Joueur():
    
    def __init__(self,idJoueur,nbrBut,nbrPasseD):
        self.idJoueur=idJoueur
        self.nbrBut=nbrBut
        self.nbrPasseD=nbrPasseD
        
    def nbr_but(joueur):
        nbrBut=cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idJoueur =" + joueur.idJoueur)
        return nbrBut
    
    
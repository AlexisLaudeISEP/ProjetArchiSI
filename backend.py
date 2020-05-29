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

## FONCTION SANS CLASSE
def dif_but_id(idEquipe):
    chaine = str(idEquipe)
    nbrButMarque = 0
    nbrButPrisDom = 0
    nbrButPrisExt = 0
    cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe = "+chaine)
    for row in cursor:
        nbrButMarque = row[0]
    cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 = "+chaine)
    for row in cursor:
        nbrButPrisDom = row[0]
    cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = "+chaine)
    for row in cursor:
          nbrButPrisExt = row[0]
        
    return (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))

def clean_shit(idEquipe):
    chaine = str(idEquipe)
    cursor.execute("SELECT COUNT(*) as Clean_sheet FROM Schema1.Match WHERE (idEquipe1 "+ chaine +" AND butEquipe2= 0) OR (idEquipe2 = <idEquipe> AND butEquipe1= 0) ")
    for row in cursor:
          nbrCleanShit = row[0]
    return nbrCleanShit

def plus_de_deux_but(idEquipe):
    chaine = str(idEquipe)
    cursor.execute("SELECT COUNT(*) FROM Schema1.Match WHERE (idEquipe1 = " + chaine +" AND butEquipe1>2) OR (idEquipe2 = "+chaine+" AND butEquipe2> 2)")
    for row in cursor:
          nbrProlifique = row[0]
    return nbrProlifique

def result(idEquipe, row):
    if idEquipe == row[1]:
        if row[2]>row[4]:
            return 'V'
        elif row[2]==row[4]:
            return 'N'
        else:
            return 'D'
    if idEquipe == row[3]:
        if row[4]>row[2]:
            return 'V'
        elif row[4]==row[2]:
            return 'N'
        else:
            return 'D'
    else:
        print('Il y a une erreur')
        
def derniersmatchs(idEquipe):
    chaine= str(idEquipe)
    cursor.execute("SELECT * FROM Schema1.Match WHERE idEquipe1="+ chaine  +" OR  idEquipe2="+ chaine + " ORDER BY Date DESC LIMIT 5")
    res=[]
    for row in cursor:
        res.append(result(idEquipe,row))
    return res

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
        cursor.execute("SELECT COUNT(*) FROM Schema1.Match WHERE idEquipe1 = "+ equipe.idEquipe + "AND butEquipe1>butEquipe2")
        for row in cursor:
            NbrVictoire= row[0]
        cursor.execute("SELECT COUNT(*) FROM Schema1.Match WHERE idEquipe1 ="+ equipe.idEquipe +" AND butEquipe1=butEquipe2")
        for row in cursor:
            NbrNul= row[0]
        return (NbrVictoire*3)+ NbrNul
    
    
    def dif_but(equipe):
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe ="+equipe.idEquipe)
        for row in cursor:
            nbrButMarque= row[0]
        cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 ="+ equipe.idEquipe)
        for row in cursor:
            nbrButPrisDom= row[0]
        cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = "+ equipe.idEquipe)
        for row in cursor:
            nbrButPrisExt= row[0]
        return (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))
    
    def but_premiere_mitemps(equipe):
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE CSC=0 AND idEquipe ="+equipe.idEquipe)
        for row in cursor:
            nbrButMarque= row[0]
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE Minute<45 AND CSC=0 AND idEquipe ="+equipe.idEquipe)
        for row in cursor:
            nbrButPremiere= row[0]
        
    

class Joueur():
    
    def __init__(self,idJoueur,nbrBut,nbrPasseD):
        self.idJoueur=idJoueur
        self.nbrBut=nbrBut
        self.nbrPasseD=nbrPasseD
        
    def nbr_but(joueur):
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idJoueur =" + joueur.idJoueur)
        for row in cursor:
            nbrBut= row[0]
        return nbrBut
    
    
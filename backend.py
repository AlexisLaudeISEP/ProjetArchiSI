#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:02:48 2020

@author: jullian
"""

import mysql.connector
from operator import itemgetter

conn = mysql.connector.connect(host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
                               user="adminSI", password="mypasswordarchis!",
                               database="Schema1")
cursor = conn.cursor()


## FONCTION SANS CLASSE
def liste_championnat():
    cursor.execute("SELECT idChampionnat, nom FROM Championnat")
    return cursor


def liste_equipe(idChampionnat):
    chaine = str(idChampionnat)
    cursor.execute("SELECT idEquipe, nom FROM Equipe WHERE idChampionnat =" + chaine)
    return cursor


def liste_buteur(idChampionnat):
    chaine = str(idChampionnat)
    cursor.execute(
        "SELECT DISTINCT nomButeur FROM Schema1.Buteur INNER JOIN Equipe ON Buteur.idEquipe = Equipe.idEquipe WHERE Equipe.idChampionnat = " + chaine)
    return cursor



def nbr_but_joueur(nomJoueur):
    cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE nomButeur = '" + nomJoueur + "' AND CSC = 0")
    for row in cursor:
        nbrBut = row[0]
    return nbrBut


def dif_but_id(idEquipe):
    chaine = str(idEquipe)
    nbrButMarque = 0
    nbrButPrisDom = 0
    nbrButPrisExt = 0
    cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe = " + chaine)
    for row in cursor:
        nbrButMarque = row[0]
    cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 = " + chaine + "AND ButEquipe1 != -1")
    for row in cursor:
        nbrButPrisDom = row[0]
    cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = " + chaine + "AND ButEquipe1 != -1")
    for row in cursor:
        nbrButPrisExt = row[0]

    return (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))


def clean_sheet(idEquipe):
    chaine = str(idEquipe)
    cursor.execute(
        "SELECT COUNT(*) FROM Schema1.Match WHERE (idEquipe1 = " + chaine + " AND butEquipe2= 0) OR (idEquipe2 = " + chaine + " AND butEquipe1= 0) ")
    for row in cursor:
        nbrCleanSheet = row[0]
    return nbrCleanSheet


def plus_de_deux_but(idEquipe):
    chaine = str(idEquipe)
    cursor.execute(
        "SELECT COUNT(*) FROM Schema1.Match WHERE (idEquipe1 = " + chaine + " AND butEquipe1>2) OR (idEquipe2 = " + chaine + " AND butEquipe2> 2)")
    for row in cursor:
        nbrProlifique = row[0]
    return nbrProlifique


def result(idEquipe, row):
    if idEquipe == row[1]:
        if row[2] > row[4]:
            return 'V'
        elif row[2] == row[4]:
            return 'N'
        else:
            return 'D'
    if idEquipe == row[3]:
        if row[4] > row[2]:
            return 'V'
        elif row[4] == row[2]:
            return 'N'
        else:
            return 'D'
    else:
        print('Il y a une erreur')


def derniersmatchs(idEquipe):
    chaine = str(idEquipe)
    cursor.execute(
        "SELECT * FROM Schema1.Match WHERE (idEquipe1=" + chaine + " OR  idEquipe2=" + chaine + ") AND ButEquipe1 != -1 ORDER BY Date DESC LIMIT 5")
    res = []
    for row in cursor:
        res.append(result(idEquipe, row))
    return res


def no_loose(idEquipe):
    chaine = str(idEquipe)
    cursor.execute(
        "SELECT * FROM Schema1.Match WHERE (idEquipe1=" + chaine + " OR idEquipe2=" + chaine + ") AND ButEquipe1 != -1 ORDER BY Date DESC ")
    res = []
    for row in cursor:
        res.append(result(idEquipe, row))
    i = 0
    count = 0
    while ((res[i] == 'V') or (res[i] == 'N')) and (i < len(res)):
        count += 1
        i += 1
    return count


def no_win(idEquipe):
    chaine = str(idEquipe)
    cursor.execute(
        "SELECT * FROM Schema1.Match WHERE (idEquipe1=" + chaine + " OR idEquipe2=" + chaine + ") AND ButEquipe1 != -1 ORDER BY Date DESC ")
    res = []
    for row in cursor:
        res.append(result(idEquipe, row))
    i = 0
    count = 0
    while ((res[i] == 'D') or (res[i] == 'N')) and i < len(res):
        count += 1
        i += 1
    return count


def ratio_but(idEquipe):
    chaine = str(idEquipe)
    cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe =" + chaine)
    for row in cursor:
        nbrButMarque = row[0]
    cursor.execute(
        "SELECT COUNT(*) FROM Schema1.Match WHERE (idEquipe1=" + chaine + " OR  idEquipe2=" + chaine + ") AND ButEquipe1 != -1")
    for row in cursor:
        nbrMatch = row[0]
    return (nbrButMarque / nbrMatch)


def nbr_point(idEquipe):
    chaine = str(idEquipe)
    count = 0
    res = []
    cursor.execute(
        "SELECT * FROM Schema1.Match WHERE (idEquipe1=" + chaine + " OR idEquipe2=" + chaine + ") AND ButEquipe1 != -1 ORDER BY Date DESC ")
    for row in cursor:
        res.append(result(idEquipe, row))
    for i in range(len(res)):
        if res[i] == 'V':
            count += 3
        if res[i] == 'N':
            count += 1
    return count


def dif_but(idequipe):

    chaine = str(idequipe)
    cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE idEquipe =" + chaine)
    for row in cursor:
        nbrButMarque = row[0]
    cursor.execute("SELECT SUM(butEquipe2) FROM Schema1.Match WHERE idEquipe1 =" + chaine)
    for row in cursor:
        nbrButPrisDom = row[0]
    cursor.execute("SELECT SUM(butEquipe1) FROM Schema1.Match WHERE idEquipe2 = " + chaine)
    for row in cursor:
        nbrButPrisExt = row[0]
    return (nbrButMarque - (nbrButPrisDom + nbrButPrisExt))


##Classe Equipe
class Equipe():

    def __init__(self, idEquipe, point, dif):
        self.idEquipe = idEquipe
        self.point = point
        self.dif = dif

    def classement(idChampionnat):
        chaine = str(idChampionnat)
        cursor.execute("SELECT idEquipe FROM Equipe WHERE idChampionnat = " + chaine)
        tab = []
        for row in cursor:
            tab.append(Equipe(row[0], nbr_point(row[0]), dif_but(row[0])))
        s = sorted(tab, key=itemgetter(2), reverse=True)
        data = sorted(s, key=itemgetter(1), reverse=True)
        return data

    def but_premiere_mitemps(equipe):
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE CSC=0 AND idEquipe =" + equipe.idEquipe)
        for row in cursor:
            nbrButMarque = row[0]
        cursor.execute("SELECT COUNT(*) FROM Schema1.Buteur WHERE Minute<45 AND CSC=0 AND idEquipe =" + equipe.idEquipe)
        for row in cursor:
            nbrButPremiere = row[0]






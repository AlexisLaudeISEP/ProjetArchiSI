import marshal
import datetime

import mysql.connector

conn = mysql.connector.connect(

    host="archisi-db.cqozp8kc5eik.eu-west-3.rds.amazonaws.com",
    user="adminSI",
    port=3306,
    password="mypasswordarchis!",
    database="Schema1"

)

conn.autocommit = False

def DicoChamp():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Championnat""")

    dictionnaireChamp = {}
    for row in cursor:
        dictionnaireChamp[row[1]] = row[0]

    print(dictionnaireChamp)
    return dictionnaireChamp





def creationTableauEquipeChamp(data) :
    listeEquipe = []
    for i in data:
        for journee in i :
            for match in journee:
                if journee[match]['equipe1'] not in listeEquipe :
                    listeEquipe.append(journee[match]['equipe1'])
    return listeEquipe

""" Bundesliga Liga Ligue-1 Serie-A"""

def injectionEquipeBDD(championnat,data):

    cursor = conn.cursor()

    listeEquipe = creationTableauEquipeChamp(data)
    dicoChamp = DicoChamp()
    idChamp = dicoChamp[championnat]

    data=[]
    for equipe in listeEquipe :
        data.append((equipe.lower(),idChamp))
    cursor.executemany("""INSERT INTO Equipe(Nom, idChampionnat) VALUES(%s, %s)""", data)
    conn.commit()
    print('insertion réussi')


def injectionAllEquipe():

    data = marshal.load(open("binaryDataChamp/dataLigue1", "rb"))
    injectionEquipeBDD('Ligue-1', data)
    data = marshal.load(open("binaryDataChamp/dataLiga", "rb"))
    injectionEquipeBDD('Liga', data)
    data = marshal.load(open("binaryDataChamp/dataBundes", "rb"))
    injectionEquipeBDD('Bundesliga', data)
    data = marshal.load(open("binaryDataChamp/dataSerieA", "rb"))
    injectionEquipeBDD('Serie-A',data)

    print (' toute les équipes ont été ajoutées')

def crationDicoEquipeID():
    cursor = conn.cursor()
    cursor.execute("""SELECT idEquipe , Nom  FROM Equipe""")
    dictionnaireEquipeID = {}
    for row in cursor:
        dictionnaireEquipeID[row[1]] = row[0]
    return  dictionnaireEquipeID


def modifDate(date):
    dateL = date.split(' ')
    if dateL[2] == 'janvier':
        moi = 1
    if dateL[2] == 'février':
        moi = 2
    if dateL[2] == 'mars':
        moi = 3
    if dateL[2] == 'avril':
        moi = 4
    if dateL[2] == 'mai':
        moi = 5
    if dateL[2] == 'juin':
        moi = 6
    if dateL[2] == 'juillet':
        moi = 7
    if dateL[2] == 'août':
        moi = 8
    if dateL[2] == 'septembre':
        moi = 9
    if dateL[2] == 'octobre':
        moi = 10
    if dateL[2] == 'novembre':
        moi = 11
    if dateL[2] == 'décembre':
        moi = 12
    date = datetime.datetime(int(dateL[3]), moi, int(dateL[1]))
    return date.date().isoformat()

def creationListeDataToInsert(data):
    dataMatch = []
    dicoEquipe = crationDicoEquipeID()
    for i in data:
        for journee in i :
            for match in journee:
                idMatch = int(match)
                idEquipe1 = dicoEquipe[journee[match]['equipe1'].lower()]
                ButEquipe1 = journee[match]['butEq1']
                idEquipe2 = dicoEquipe[journee[match]['equipe2'].lower()]
                ButEquipe2 = journee[match]['butEq2']
                Date = modifDate(journee[match]['jour'])
                if (idMatch,idEquipe1,ButEquipe1,idEquipe2,ButEquipe2,Date) not in dataMatch :
                    dataMatch.append((idMatch,idEquipe1,ButEquipe1,idEquipe2,ButEquipe2,Date))
    return dataMatch

def insertMatchInBdd(data):
    cursor = conn.cursor()
    data = creationListeDataToInsert(data)

    cursor.executemany("""INSERT INTO Schema1.Match(idMatch, idEquipe1, ButEquipe1, idEquipe2, ButEquipe2,Date) VALUES(%s, %s,%s, %s,%s, %s)""", data)
    conn.commit()

def injectionAllMatch():

    data = marshal.load(open("binaryDataChamp/dataLigue1", "rb"))
    insertMatchInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataLiga", "rb"))
    insertMatchInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataBundes", "rb"))
    insertMatchInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataSerieA", "rb"))
    insertMatchInBdd(data)


def creationListeDataToInsertButeur(data):
    listebuteur = []
    dicoEquipe = crationDicoEquipeID()
    for i in data:
        for journee in i :
            for match in journee:
                if journee[match]['buteurEq1'] !=[]:
                    for i in journee[match]['buteurEq1']:
                        idMatch = int(match)
                        idEquipe = dicoEquipe[journee[match]['equipe1'].lower()]
                        minute = int(i[2])
                        buteur = i[1]
                        if i[3] == 'CSC' :
                            CSC = 1
                            penalty = 0
                        elif i[3] == 'penalty':
                            CSC = 0
                            penalty = 1
                        else :
                            CSC = 0
                            penalty = 0
                        if (idMatch,idEquipe,minute,penalty,CSC,buteur) not in listebuteur :
                            listebuteur.append((idMatch,idEquipe,minute,penalty,CSC,buteur))
                else:
                    pass

                if journee[match]['buteurEq2'] !=[]:
                    print(journee[match]['buteurEq2'])
                    for i in journee[match]['buteurEq2'] :
                        idMatch = int(match)
                        idEquipe = dicoEquipe[journee[match]['equipe2'].lower()]
                        minute = int(i[2])
                        buteur = i[1]
                        if i[3] == 'CSC' :
                            CSC = 1
                            penalty = 0
                        elif i[3] == 'penalty':
                            CSC = 0
                            penalty = 1
                        else :
                            CSC = 0
                            penalty = 0
                        if (idMatch, idEquipe, minute, penalty, CSC, buteur) not in listebuteur:
                            listebuteur.append((idMatch,idEquipe,minute,penalty,CSC,buteur))
                else:
                    pass
    return listebuteur


def insertButeurInBdd(data):
    cursor = conn.cursor()
    data = creationListeDataToInsertButeur(data)
    cursor.executemany("""INSERT INTO Schema1.Buteur(idMatch, IdEquipe, Minute, Penalty, CSC, nomButeur) VALUES(%s, %s,%s, %s,%s, %s)""", data)
    conn.commit()


def injectionAllButeur():

    data = marshal.load(open("binaryDataChamp/dataLigue1", "rb"))
    insertButeurInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataLiga", "rb"))
    insertButeurInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataBundes", "rb"))
    insertButeurInBdd(data)
    data = marshal.load(open("binaryDataChamp/dataSerieA", "rb"))
    insertButeurInBdd(data)

#injectionAllEquipe()
#injectionAllMatch()
injectionAllButeur()









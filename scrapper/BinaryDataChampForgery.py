import marshal
from scrapper import dataChamp


def BinaryDataCreation (championnat) :

    dossier = 'binaryDataChamp/'

    if championnat == 'ligue-1' :
        dataC = dataChamp.dataChamp('france', championnat)
        chemin = dossier + 'dataLigue1'
    elif championnat == 'primera-division' :
        dataC =  dataChamp.dataChamp('espagne', championnat)
        chemin = dossier + 'dataLiga'
    elif championnat == 'bundesliga-1' :
        dataC = dataChamp.dataChamp('allemagne', championnat)
        chemin = dossier + 'dataBundes'
    elif championnat == 'serie-a' :
        dataC = dataChamp.dataChamp('italie', championnat)
        chemin = dossier + 'dataSerieA'

    dataC.creatData()
    data = dataC.data
    print(data)
    #marshal.dump(data, open(chemin, 'wb'))  ## Sauvegarde


BinaryDataCreation('ligue-1')
#BinaryDataCreation('primera-division')
#BinaryDataCreation('bundesliga-1')
#BinaryDataCreation('serie-a')



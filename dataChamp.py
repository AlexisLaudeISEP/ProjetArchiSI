import scrapper
import json
import marshal

class dataChamp(object):

    def __init__(self,pays,championnat):
        self.championnat = championnat
        self.url = '/' + pays + '/' + championnat
        self.data = []

    def creatTablePage(self):
        table = []

        for i in range(32,52):
            table.append('/2019-'+ str(i))
        for j in range(2,10):
            table.append('/2020-0'+ str(j))
        for k in range(10,22):
            table.append('/2020-' + str(k))

        return table

    def creatData(self):

        tablePage= self.creatTablePage()

        for i in tablePage:
            page = scrapper.scoreMatch('https://www.matchendirect.fr/', self.url + i ,self.championnat)
            page.getData()
            parsedHtml = page.parseList()
            if parsedHtml != [] :
                self.data.append(parsedHtml)

"""
dataChampLigue1 = dataChamp('france' , 'ligue-1')
dataChampLigue1.creatData()
dataLigue1 = dataChampLigue1.data

marshal.dump(dataLigue1, open("dataLigue1", 'wb')) ## Sauvegarde
"""

"""
dataChampLiga = dataChamp('espagne' , 'primera-division')
dataChampLiga.creatData()
dataLiga = dataChampLiga.data

marshal.dump(dataLiga, open("dataLiga", 'wb')) ## Sauvegarde

"""
"""
dataChampBundes = dataChamp('allemagne' , 'bundesliga-1')
dataChampBundes.creatData()
dataBundes = dataChampBundes.data

marshal.dump(dataBundes, open("dataBundes", 'wb')) ## Sauvegarde

"""
dataChampSerieA = dataChamp('italie' , 'serie-a')
dataChampSerieA.creatData()
dataSerieA = dataChampSerieA.data

marshal.dump(dataSerieA, open("dataSerieA", 'wb')) ## Sauvegarde




"""
france       ligue-1
allemagne    bundesliga-1
angleterre   barclays-premiership-premier-league
espagne      primera-division
italie       serie-a

"""
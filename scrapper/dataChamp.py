from scrapper import scrapping
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
            page = scrapping.scoreMatch('https://www.matchendirect.fr/', self.url + i ,self.championnat)
            page.getData()
            parsedHtml = page.parseList()
            if parsedHtml != [] :
                self.data.append(parsedHtml)



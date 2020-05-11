import scrapper
import json


def creatTablePage():
    table = []
    for i in range(32,52):
        table.append('/2019-'+ str(i))
    for j in range(2,10):
        table.append('/2020-'+ str(j))
    return table

tablePage=creatTablePage()

for i in range(tablePage):

    page = scrapper.scoreMatch('https://www.matchendirect.fr/', '/france/ligue-1' + i )
    html = page.getData()
    parsedHtml = page.parseList()
    parsedJson = json.dumps(parsedHtml)

print(tablePage)
"""
def creatAllDataScoreMatch(tableau):




print(parsedJson)
"""
""" www.matchendirect.fr/france/ligue-1//2019/-32 --> 51 au www.matchendirect.fr/france/ligue-1//2020 au /2020-21/ """
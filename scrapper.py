"""
fonctions de récupération de la page html et parsing des données

"""



import requests
from bs4 import BeautifulSoup
import json


class scoreMatch(object):

    def __init__(self ,domain, partOfTheSite):
        self.url = domain + partOfTheSite

    def getData(self):
        html = requests.get(self.url).text
        self.soup = BeautifulSoup(html, 'html.parser')


    def parseList(self):
        tableau = self.soup.find('div',{ 'id' : 'livescore'}).find_all('tr')
        dataList = []
        data = {}
        for match in tableau:
            data = {}
            if (match.find('td',{ 'class':'lm1'})!= None):
                data['heure']= match.find('td',{ 'class':'lm1'}).text
                data['temps'] = match.find('td',{ 'class':'lm2'}).text
                data['equipe1'] = match.find('span', {'class': 'lm3_eq1'}).text
                data['score'] = match.find('span', {'class': 'lm3_score'}).text
                data['equipe2'] = match.find('span', {'class': 'lm3_eq2'}).text
                dataList.append(data)
        return dataList


    """
    def cleanList(self, list):
        modifiedList =[]
        for i in list:
            modifiedList.append(list[i].replace('équipe', 'equipe'))
        return modifiedList
    """






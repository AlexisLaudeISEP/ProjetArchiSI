"""
fonctions de récupération de la page html et parsing des données
"""

import urllib
import requests
from bs4 import BeautifulSoup
import json


class scoreMatch(object):

    def __init__(self ,domain, partOfTheSite, ligue):
        self.url = domain + partOfTheSite
        self.ligue = ligue
        self.urlValide =False


    def getData(self):
        with urllib.request.urlopen(self.url) as page:
            data = page.read().decode('utf-8')
        self.soup = BeautifulSoup(data, 'html.parser')


    def parseList(self):
        print(self.url)
        tableau = self.soup.find('div',{ 'id' : 'livescore'}).find_all('tr')
        dataList = []
        data = {}
        for match in tableau:

            matchDic = {}

            if (match.find('td',{ 'class':'lm1'})== None):
                jour = match.find('th').text

            else:

                score = match.find('span', {'class': 'lm3_score'}).text
                sep = score.split('-')
                id = match['data-matchid']

                matchDic['jour'] = jour
                matchDic['heure']= match.find('td',{ 'class':'lm1'}).text
                matchDic['temps'] = match.find('td',{ 'class':'lm2'}).text

                if self.ligue == 'ligue-1' :
                    matchDic['equipe1'] = self.cleanUrlLigue1(match.find('span', {'class': 'lm3_eq1'}).text)

                if self.ligue == 'primera-division':
                    matchDic['equipe1'] = self.cleanUrlLiga(match.find('span', {'class': 'lm3_eq1'}).text)

                if self.ligue == 'serie-a':
                    matchDic['equipe1'] = self.cleanUrlSerieA(match.find('span', {'class': 'lm3_eq1'}).text)

                if self.ligue == 'bundesliga-1':
                    matchDic['equipe1'] = self.cleanUrlBundes(match.find('span', {'class': 'lm3_eq1'}).text)

                if self.ligue == 'barclays-premiership-premier-league':
                    matchDic['equipe1'] = self.cleanUrlpremierLigue(match.find('span', {'class': 'lm3_eq1'}).text)


                try :
                    matchDic['butEq1']= int(sep[0])
                except :
                    matchDic['butEq1'] = -1

                matchDic['buteurEq1']=[]

                if self.ligue == 'ligue-1' :
                    matchDic['equipe2'] = self.cleanUrlLigue1(match.find('span', {'class': 'lm3_eq2'}).text)

                if self.ligue == 'primera-division':
                    matchDic['equipe2'] = self.cleanUrlLiga(match.find('span', {'class': 'lm3_eq2'}).text)

                if self.ligue == 'serie-a':
                    matchDic['equipe2'] = self.cleanUrlSerieA(match.find('span', {'class': 'lm3_eq2'}).text)

                if self.ligue == 'bundesliga-1':
                    matchDic['equipe2'] = self.cleanUrlBundes(match.find('span', {'class': 'lm3_eq2'}).text)

                if self.ligue == 'barclays-premiership-premier-league':
                    matchDic['equipe2'] = self.cleanUrlpremierLigue(match.find('span', {'class': 'lm3_eq2'}).text)




                try :
                    matchDic['butEq2'] = int(sep[1])
                except :
                    matchDic['butEq2'] = -1

                matchDic['buteurEq2'] = []

                data[id]=matchDic

                dataList.append(data)


                if matchDic['butEq1'] + matchDic['butEq2'] > 0 :

                    domain = 'https://www.matchendirect.fr/foot-score'

                    if self.ligue == 'ligue-1' :
                        subD = '/' + id + '-' + matchDic['equipe1'] + '-' + matchDic['equipe2'] + '.html'

                        scorePage = scoreMatch(domain, subD, self.ligue)
                        scorePage.getData()
                        buteur = scorePage.parseListScore2()

                    else:
                        try :
                            subD = '/' + id + '-' + matchDic['equipe1'] + '-' + matchDic['equipe2'] + '.html'
                            subDB = '/' + id + '-' + matchDic['equipe2'] + '-' + matchDic['equipe1'] + '.html'

                            try:
                                #print('1')
                                scorePage = scoreMatch(domain, subD, self.ligue)
                                scorePage.getData()
                                buteur = scorePage.parseListScore2()
                                #print(domain+subD)
                                #print(buteur)

                            except:
                                #print('2')
                                scorePage = scoreMatch(domain, subDB, self.ligue)
                                scorePage.getData()
                                buteur = scorePage.parseListScore2()
                                #print(domain + subDB)
                                #print(buteur)



                        except :
                            subD = '/'+ matchDic['equipe1'] + '-' + matchDic['equipe2'] + '.html'
                            subDB = '/'+ matchDic['equipe2'] + '-' + matchDic['equipe1'] + '.html'

                            try:
                                #print('3')
                                scorePage = scoreMatch(domain, subD, self.ligue)
                                scorePage.getData()
                                buteur = scorePage.parseListScore2()
                                #print(domain + subD)
                                #print(buteur)

                            except:
                                #print('4')
                                scorePage = scoreMatch(domain, subDB, self.ligue)
                                scorePage.getData()
                                buteur = scorePage.parseListScore2()
                                #print(domain + subDB)
                                #print(buteur)

                    for i in buteur:
                        if i[0]=='equipe1':
                            matchDic['buteurEq1'].append(i)
                        else:
                            matchDic['buteurEq2'].append(i)
        return dataList

    def parseListScore2(self):
        list = []
        tableau = self.soup.find('table', {'id': 'match_evenement'}).find_all('tr')
        for tr in tableau :
            try :
                if len(tr.find('td', {'class': 'c3'}).text) ==1 :
                    try:
                        classBalise = tr.find('td', {'class': 'c1'}).find('span')['class']
                        if 'ico_evenement1' in classBalise:
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c1'}).find('a').text
                            equipe = 'equipe1'
                            evenement = 'butNormal'
                            list.append([equipe, buteur, minuteBut, evenement])
                        if 'ico_evenement2' in classBalise:
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c1'}).find('a').text
                            equipe = 'equipe1'
                            evenement = 'penalty'
                            list.append([equipe, buteur, minuteBut, evenement])
                        if 'ico_evenement7' in classBalise:
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c1'}).find('a').text
                            equipe = 'equipe1'
                            evenement = 'CSC'
                            list.append([equipe, buteur, minuteBut, evenement])
                    except:
                        pass
                else:
                    self.urlValide = True
                    try :
                        classBalise =tr.find('td',{'class':'c3'}).find('span')['class']
                        if 'ico_evenement1' in classBalise :
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c3'}).find('a').text
                            equipe = 'equipe2'
                            evenement = 'butNormal'
                            list.append([equipe, buteur, minuteBut,evenement])
                        if 'ico_evenement2' in classBalise:
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c3'}).find('a').text
                            equipe = 'equipe2'
                            evenement = 'penalty'
                            list.append([equipe, buteur, minuteBut,evenement])
                        if 'ico_evenement7'in classBalise:
                            minuteBut = (tr.find('td', {'class': 'c2'}).text).split('\'')[0]
                            buteur = tr.find('td', {'class': 'c3'}).find('a').text
                            equipe = 'equipe2'
                            evenement = 'CSC'
                            list.append([equipe, buteur, minuteBut,evenement])
                    except:
                        pass
            except:
                pass


        return list

    """ V1 du parser avec ces 2 fonctions / plus utile ...
    *
    *
    *
    def parseListScore(self):
        list = []
        tableau = self.soup.find('div', {'id': 'scroll_commentaire'}).find_all('tr', {'class': 'ct2'})
        for but in tableau :
            parsing = but.find_all('td')
            minuteBut = parsing[0].text
            textBut = parsing[2].text
            if "BUT" in textBut :
                textBut = textBut.split('!', 1)[0]
                textBut = textBut.split('de', 1)[1]
                listButeurClub = textBut.split('pour')
                listButeurClub.append(minuteBut)
                list.append(listButeurClub)
        return list
     """

    def cleanUrlLigue1(self,txt):
        if txt == 'Olympique Lyonnais' :
            return txt.replace('Olympique Lyonnais', 'lyon')
        if txt == 'Olympique Marseille':
            return txt.replace('Olympique Marseille', 'marseille')
        if txt == 'PSG':
            return txt.replace('PSG', 'paris-saint-germain')
        if txt == 'Nîmes':
            return txt.replace('Nîmes','nimes')
        if txt == 'Saint-Étienne':
            return txt.replace('Saint-Étienne', 'saint-etienne')
        if txt == 'Amiens SC':
            return txt.replace('Amiens SC' , 'amiens')
        else:
            return txt

    def cleanUrlLiga(self,txt):
        if txt == 'Grenade' :
            return txt.replace('Grenade', 'granada-cf')
        if txt == 'Espanyol':
            return txt.replace('Espanyol', 'espanyol-barcelone')
        if txt == 'Real Madrid':
            return txt.replace('Real Madrid', 'real-madrid')
        if txt == 'Atlético Madrid':
            return txt.replace('Atlético Madrid','atletico-madrid')
        if txt == 'Real Valladolid':
            return txt.replace('Real Valladolid', 'real-valladolid')
        if txt == 'Celta Vigo':
            return txt.replace('Celta Vigo' , 'celta-vigo')
        if txt == 'Real Sociedad':
            return txt.replace('Real Sociedad' , 'real-sociedad')
        if txt == 'Real Bétis':
            return txt.replace('Real Bétis' , 'real-betis')
        if txt == 'Athletic Bilbao':
            return txt.replace('Athletic Bilbao' , 'athletic-bilbao')
        if txt == 'Deportivo Alavés':
            return txt.replace('Deportivo Alavés' , 'deportivo-alaves')
        if txt == 'Séville':
            return txt.replace('Séville','seville')
        else:
            return txt

    def cleanUrlSerieA(self, txt):
        if txt == 'Sampdoria':
            return txt.replace('Sampdoria', 'sampdoria-de-genes')
        if txt == 'Hellas Verona':
            return txt.replace('Hellas Verona', 'verone')
        if txt == 'Rome':
            return txt.replace('Rome', 'roma')
        if txt == 'Atalanta':
            return txt.replace('Atalanta', 'atalanta-bergame')
        if txt == 'Juventus':
            return txt.replace('Juventus', 'juventus-de-turin')
        if txt == 'Lazio':
            return txt.replace('Lazio', 'lazio-rome')
        if txt == 'Inter Milan':
            return txt.replace('Inter Milan', 'inter-milan')
        else:
            return txt


    def cleanUrlBundes(self, txt):
        if txt == 'Werder Brême':
            return txt.replace('Werder Brême', 'werder-breme')
        if txt == 'Bayer Leverkusen':
            return txt.replace('Bayer Leverkusen', 'bayer-leverkusen')
        if txt == 'Hertha BSC':
            return txt.replace('Hertha BSC', 'hertha-berlin')
        if txt == 'Union Berlin':
            return txt.replace('Union Berlin', 'union-berlin')
        if txt == 'Borussia M\'gladbach':
            return txt.replace('Borussia M\'gladbach', 'borussia-m-gladbach')
        if txt == 'Borussia Dortmund':
            return txt.replace('Borussia Dortmund', 'borussia-dortmund')
        if txt == 'Fribourg':
            return txt.replace('Fribourg', 'freiburg')
        if txt == 'Bayern Munich':
            return txt.replace('Bayern Munich', 'bayern-munich')
        if txt == 'Schalke 04':
            return txt.replace('Schalke 04', 'schalke-04')
        if txt == 'Mainz 05':
            return txt.replace('Mainz 05', 'fsv-mayence')
        if txt == 'RB Leipzig':
            return txt.replace('RB Leipzig', 'rb-leipzig')
        if txt == 'Cologne':
            return txt.replace('Cologne', 'fc-cologne')
        if txt == 'Fortuna Düsseldorf':
            return txt.replace('Fortuna Düsseldorf', 'fortuna-dusseldorf')
        if txt == 'Wolfsbourg':
            return txt.replace('Wolfsbourg', 'wolfsburg')
        if txt == 'Augsbourg':
            return txt.replace('Augsbourg', 'augsburg')
        if txt == 'Eintracht Francfort':
            return txt.replace('Eintracht Francfort', 'eintracht-francfor')
        else:
            return txt

"""
test = scoreMatch('https://www.matchendirect.fr/allemagne/bundesliga-1','/2019-43/','bundesliga-1')
test.getData()
print(test.parseList())"""
# le programme de scraping avec python 3
#importation des bibliotheques necessaires
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import csv  
N=5# Nombre de pages á scraper
PrixDefaut=500000 # Prix par defaut des autos qui n'ont pas de prix
url="http://www.expat-dakar.com/annonces/autos-occasions-1.html?page={}" # L'url de la page á scraper
with open('ListeAUTOS.csv', 'w') as csvfile: #Ouverture du fichier CSV pour l'ecriture
    fieldnames = ['Noms', 'Prix'] # Entete deu fichier CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for I in range(1,N): #Boucle pour parcourir les differente pages web
        URL=urllib.request.urlopen(url.format(I))# Acces a la page
        InfoUtile=BeautifulSoup(URL.read(),"html.parser").findAll('div',{'class':'annonce_gauche'})# recuperation de chaque zone contenant les informations utile pour la resolution de noter proble
        for InfoU in InfoUtile: #parcourir les differents de la zone reperé
            NOM=InfoU.find('span').get_text() #recuperation de nom de l'auto
            try:
                PRIX= InfoU.find('div',class_='picto prix').get_text() # recuperation du prix de l'auto
            except AttributeError:
                PRIX=PrixDefaut # assignation de la valeur par defaut au prix
            writer.writerow({'Noms':NOM , 'Prix':PRIX }) # ecriture du Nom et du prix de chaque auto dans le fichier CSV
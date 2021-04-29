import csv
import collections as Counter
from os import close 
#no me funciona, pero te lo mando igual, espero una respuesta..
archivo = open('appstore_games.csv', 'r', encoding='utf-8')   
csvreader = csv.reader(archivo, delimiter=',')
def modulo1():    
    spain_free= filter(lambda x: x[13] == "ES"and x[9]==0,csvreader)   #filtro si el juego esta en ES y es gratis
    for elem in spain_free:
        print(f"{elem[3]:<40}") #imprimo los nombres de los juegos en ESyfree


def modulo2():
    for elem in csvreader[8]:
        max=Counter(elem).most_common(10)
        
modulo1()
archivo.close()
import csv
import json
def camas():
    archivo=open("camas-criticas.csv", 'r', encoding='utf-8') 
    csvreader= csv.reader (archivo, delimiter =',')
    f = open('camas.json', 'w')
    datos_cama= list(filter(lambda x: x[1] == "LA PLATA" and x[5] > '2012',csvreader)) 
    for elem in datos_cama:
        json.dump(elem,f)
    f.close()
camas()   
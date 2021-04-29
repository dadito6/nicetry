import csv
import json
def agencia():
    archivo=open("agencia-viajes.csv", 'r', encoding='utf-8') 
    csvreader= csv.reader (archivo, delimiter =',')
    f = open('agencia.json', 'w')
    agencias_misiones= list(filter(lambda x: x[6] == "La Plata", csvreader))
    for elem in agencias_misiones:
        json.dump(elem,f)
    f.close()
agencia()    
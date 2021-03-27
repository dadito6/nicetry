frase=input('Ingrese una frase :').split(' ')
bu=True
for letra in frase:
    if(letra.isalpha()):
            if frase.count(letra)>1:
                print('NO ES UNA FRASE HETEROGRAMA!!')              #Si la letra aparece dos veces o mas
                bu=False
    else:
        print('no es un letra..') 
if(bu==True):
    print('La frase o palabra ingresada es un heterograma :D')
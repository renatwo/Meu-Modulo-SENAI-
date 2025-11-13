import statistics
import random

def moda(lista):
    return statistics.mode(lista)

def media(lista):
    return statistics.mean(lista)
    
def desvio(lista):
    return statistics.stdev(lista)

def menor_maior(lista):
    return max(lista),min(lista)

def aleatorio():
    return random.randrange(5,11), random.randint(5,11), random.randint(5,11)


def ale_range():
    return random.randrange(10,31)

def contagem():
    for c in range(10,0,-1):
        print('contagem:', c)
    print('🔥')    

def soma_pares(x):
    s = 0
    for i in range(2,x,2):
        s  =  s  + i
        print('numeros: ',s)
    print('Soma: ', s)    


def tabuada(y):
    for i in range(1,11):
        c  =  y * i
        print(y,'x',i,'=',c)

def contagem2():
    for x in range(99,-1,-1):
        print(x)        
import meu_modolo

# main.py


def estatistica():
    lista = [1,2,3,5,6,10,10]

    moda =  meu_modolo.moda(lista)
    print('moda:', moda)


    des =  meu_modolo.desvio(lista)
    print('Desvio:', des)


    media =  meu_modolo.media(lista)
    print('media:', media)


    maior, menor =  meu_modolo.menor_maior(lista)
    print('maior:', maior,'menor:',menor )

    a,b,c = meu_modolo.aleatorio()
    print('aleatorio:', a,b,c)

    x  =  meu_modolo.ale_range()
    print('Aleatorio: ', x)

    meu_modolo.contagem()

    meu_modolo.soma_pares(6)

    meu_modolo.tabuada(21)

    meu_modolo.contagem2()

estatistica()    
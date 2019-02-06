def reconocerMatriz (prueba):
    return [y.split() for y in open (prueba, 'r')]

def moverDerecha(matriz,x,y,centinela,longitud):
        if(centinela<longitud):
            print(matriz[x][y])
            moverDerecha(matriz,x,y+1,centinela+1,longitud)
        if(centinela==longitud):
            moverAbajo(matriz,x+1,y-1,0,longitud-1)

def moverAbajo(matriz,x,y,centinela,longitud):
        if(centinela<longitud):
            print(matriz[x][y])
            moverAbajo(matriz,x+1,y,centinela+1,longitud)
        if(centinela==longitud):
            moverIzquierda(matriz,x-1,y-1,0,longitud)

def moverIzquierda(matriz,x,y,centinela,longitud):
        if(centinela<longitud):
            print(matriz[x][y])
            moverIzquierda(matriz,x,y-1,centinela+1,longitud)
        if(centinela==longitud):
            moverArriba(matriz,x-1,y+1,0,longitud-1)

def moverArriba(matriz,x,y,centinela,longitud):
        if(centinela<longitud):
            print(matriz[x][y])
            moverArriba(matriz,x-1,y,centinela+1,longitud)
        if(centinela==longitud):
            moverDerecha(matriz,x+1,y+1,0,longitud)


moverDerecha(reconocerMatriz("matriz5.txt"),0,0,0,len(reconocerMatriz("matriz5.txt")))


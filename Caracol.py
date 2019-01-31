def reconocerMatriz (prueba):
    return [y.split() for y in open (prueba, 'r')]

print (reconocerMatriz ('prueba.txt'))

def recorrerDerecha (): 
    for i in range(len(reconocerMatriz ('prueba.txt'))):
        print(reconocerMatriz('prueba.txt')[0][i], end=" ")
        
    return  


#print (reconocerMatriz ('prueba.txt')[0][0])

recorrerDerecha()
#print (recorrerMatriz())


#ordenar Lista- metodo de intercambio    
def invertir(miLista):
    inicio=0
    fin=len(miLista)-1
    while inicio<fin:
        aux=miLista[fin]
        miLista[fin]=miLista[inicio]
        miLista[inicio]=aux
        inicio=inicio +1
        fin=fin-1
        
    return miLista
        
Lista=[26,37,4,9,5,7,8,0,1,-1,24,21,16]
resultado=invertir(Lista)
print(resultado)
    
    




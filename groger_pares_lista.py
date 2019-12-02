
#lista=[1,2,3,6,5,4,7,8]
#contador=0
#n=0
#par=[]
#impar=[]
#while contador <len(lista):
#    if lista[n]%2==0:
#        par.append(lista[n])
#    else:
#        impar.append(lista[n])
#    contador=contador+1
#    n=n+1

#print('numeros pares ',par)
#print('numeros impares ',impar)

def contar(lista):
    contador=0
    n=0
    par=[]
    impar=[]
    while contador <len(lista):
        if lista[n]%2==0:
           par.append(lista[n])
        else:
           impar.append(lista[n])
        
        contador=contador+1
        n=n+1

    print('numeros pares ',par)
    print('numeros impares ',impar)

n=contar([7,8,9,5,4,1,2,6,5])    
print(n)





def celsius(valor):
    valor1=(valor*9/5)+32
    return f'o valor {valor} celsius convertido para fahrenheit é: {valor1}'

print(celcius(32))

def repetir(valor,valor1):
    valor2= valor.count(valor1)
    return f'o {valor1} se repeti: {valor2}'

print(repetir('hugo hugo hugo, erico','h'))

def media(valor,valor1,valor2,valor3):
    valor4= valor+valor1+valor2+valor3/4
    return f'a media das 4 notas é: {valor4}'

print(media(5,8,5,7))


def maior():
    lista = []
    while True:
       n = int(input('Digite o número :'))
       b = input("deseja continuar [S/N] ").upper()
       lista.append(n)
       if b == 'N':
          break
    return f' numero maior:{max(lista)}\n numero menor:{min(lista)}'
    
                      
print(maior())

import math

def area(valor):
    valor1=math.pi*(valor*valor)
    return f'a area do circula é :{round(valor1,2)}'

print(area(12))

    
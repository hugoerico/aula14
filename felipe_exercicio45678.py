def celsius(valor):
    valor1=(valor*9/5)+32
    return f'o valor {valor} celsius convertido para fahrenheit é: {valor1}'

print(celsius(int(input("digite um valor inteiro "))))

def repetir(valor,valor1):
    valor2= valor.count(valor1)
    return f'o {valor1} se repete: {valor2}'

valor=input('digite palavras separadas por espaço ')
valor1=input('digite a letra que quer saber a quantidade que se repete  ')
print(repetir(valor,valor1))

def media(valor,valor1,valor2,valor3):
    valor4= (valor+valor1+valor2+valor3)/4
    
    return f'a media das 4 notas é: {valor4}'
valor=float(input('digite o 1º valor '))
valor1=float(input('digite o 2º valor '))
valor2=float(input('digite o 3º valor '))
valor3=float(input('digite o 4º valor '))
print(media(valor,valor1,valor2,valor3))


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

    
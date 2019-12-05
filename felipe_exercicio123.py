class Valores:
    def __init__(self,valor1,valor2):
        self.valor1=valor1
        self.valor2=valor2
        
    def somar(self):
        
        return f'soma dos numeros é igual a: {self.valor1 + self.valor2}'

    def multiplicar(self):
        
        return f'multiplicação dos numeros é igual a: {self.valor1*self.valor2}'

    def par(self):
        lista=[self.valor1,self.valor2]
        contador=0
        n=0
        par=[]
        impar=[]
        while contador < len (lista):
            if lista[n]%2==0:
                par.append(lista[n])
            else:
                impar.append(lista[n])
            contador=contador+1
            n=n+1
        return f'numero par {par},numero impar {impar}'
        
       





       



exercico= Valores(valor1=int(input('digite o primeiro numero ')),valor2=int(input('digite o segundo numero ')))

print(exercico.somar())
print(exercico.multiplicar())
print(exercico.par())
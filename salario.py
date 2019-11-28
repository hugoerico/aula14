def salario(n1,n2,n3):
    soma=n2*n3/2
    print(n1,'seu salario é ',round(soma,2))

a=input('digite seu nome ')
b=float(input('digite o valor da hora trabalhado '))
c=int(input('digite as horas trabalhadas '))

salario(a,b,c)
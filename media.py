def media(n1,n2):
    nota=(n1+n2)/2
    if nota>=6:
        print("Parabéns! Você foi aprovado!")
    else:
        print("reprovado")

n6=int(input('digite a primeira nota do aluno '))
n7=int(input('digite a segunda nota do aluno '))
media(n6,n7)
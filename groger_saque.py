class Banco:
    def __init__(self,nome,idade,saldo):
        self.nome=nome
        self.idade=idade
        self.saldo=saldo
        

    def __str__(self):
        return f"nome: {self.nome}, idade: {self.idade}, saldo:{self.saldo}"

    def saque(self, valor):
        self.valor = valor
        if self.valor > self.saldo and self.valor > 1000:
            return 'Saque negado'
        else:
            self.saldo -= self.valor
            return f'aprovado. Saldo em conta: R${self.saldo}'

    def deposito(self, valor):
        self.valor = valor
        if valor > 5000:
            return 'Deposito negado'
        else:
            self.saldo += self.valor
            return f' aprovado. Saldo em conta: R${self.saldo}'

    def emprestimo(self, valor):
        self.valor = valor
        if self.idade < 21 and self.saldo > 1000 and self.valor < (self.saldo*15):
            self.saldo += self.valor
            return f' aprovado. Saldo em conta: R${self.saldo}'

pessoa = Banco(str(input('Nome completo: ')), int(input('Idade: ')), saldo=2000.00)
print('''Qual operação gostaria de realizar?:
1 Saque
2 Deposito
3 Emprestimo
Qualquer outro texto ou número Sair''')
usuario = input('digite sua opção: ')
if usuario == '1':
    print(pessoa.saque(float(input('digite o valor do saque: R$'))))
elif usuario == '2':
    print(pessoa.deposito(float(input('digite o valor do emprestimo: R$'))))
elif usuario == '3':
     print(pessoa.emprestimo(float(input('digite o valor do emprestimo: R$'))))
else :
    print('tchau')
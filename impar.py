def par(numero):
	if numero%2==0:
		return True
	elif numero%2!=0:
		return False
numero=int(input('digite um numero:'))
n=par(numero)
print(n)

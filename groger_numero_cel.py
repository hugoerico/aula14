numero=input('digite seu numero de celular ')
n=str(numero)

if len(n)==9:
  if n[0]=='9':
    print('numero aceito')
  print('numero invalido')  
else:
  print('numero invalido')

r1 = float(input('Qual o 1º lado?'))
r2 = float(input('Qual o 2º lado?'))
r3 = float(input('Qual o 3º lado?'))

if(r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Esses nºs são passiveis a formar um triângulo:')
else:
    print('Esses nºs NÂO são passíveis a formar um triângulo')
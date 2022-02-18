from math import trunc
import random
x = (random.random())*5
ale = trunc(x)
num = int(input('Digite um nº de 0 a 5 para ganhar do PC:'))
if(num > 5):
    print('Erro!! Você digitou um número menor que 5!!')
elif(num == ale):
    print('Você ganhou!!!')
elif(num != ale):
    print('PC ganhou!!!')
else:
    print('Você ta colocando o que? Uma banana?')

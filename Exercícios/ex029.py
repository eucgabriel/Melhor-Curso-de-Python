vel = int(input('Qual a velocidade do seu carro nesse momento:'))
if(vel > 80):
    km = vel - 80
    pre = km * 7.00
    print('''
          Você excedeu o limite de velocidade, chegou a {}km/h
          O que é {} a mais que o limite da via
          Com isso irá ter que pagar R${:.2f} 
          '''.format(vel, km, pre))
else:
    print('Você ta andando no limite previsto')
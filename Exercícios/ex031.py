km = int(input('Qual a distância que você irá percorrer?'))
if(km < 200):
    price = km * 0.5
    print('''
            Foi percorrido {}km
            E irá gastar R${:.2f} de passagem
          '''.format(km, price))
else:
    price = km * 0.45
    print('''
            Foi percorrido {}km
            E irá gastar R${:.2f} de passagem
          '''.format(km, price))
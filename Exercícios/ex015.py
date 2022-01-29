km = float(input('Quantos KM foram rodados com esse carro?'))
d = float(input('Agora quantos dias que ficou com ele:'))
print('''
        Quilometros rodados {:.1f}km
        Com {:.0f} dias com o veículo
        O que acarretou a pagar R$ {:.2f}
'''.format(km, d, (60*d)+(0.15*km)))

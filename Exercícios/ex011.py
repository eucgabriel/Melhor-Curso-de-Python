a = float(input('Qual a altura dessa parede?'))
l = float(input('Qual a largura dessa parede?'))
print('''
        A altura  dessa parede é {}m
        A largura dessa parede é {}m
        O que dá {:.3f}m²
        E são usados {:.1f} litros de tinta!!
'''.format(a, l, a * l, (a*l)/2))

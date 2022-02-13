n = input('Qual seu nome completo?').strip()
nome = n.split()
print('''
    O seu 1º nome é {}
    E seu último nome é {}
'''.format(nome[0],nome[len(nome)-1]))
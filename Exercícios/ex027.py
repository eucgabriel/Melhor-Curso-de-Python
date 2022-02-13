nome = input('Qual seu nome completo?')
nome_split = nome.split()
len_split = int(len(nome_split))
print('''
    O seu 1º nome é {}
    E seu último nome é {}
'''.format(nome(len_split(min)), nome(len_split(max))))

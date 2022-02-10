nome = str(input('Qual o seu nome completo?')).strip()

print('''
        {}
        {}
        Seu nome tem {} letras
        Seu 1º nome tem {} letras
'''.format(nome.upper(), nome.lower(), (len(nome)-nome.count(' ')), nome.find(' ')))
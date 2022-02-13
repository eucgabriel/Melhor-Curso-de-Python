frase = input('Escreva uma frase qualquer: ').upper()
print('''
      A frase "{}" tem {} letra(s) A(s)
      A letra 'A' aparece a primeira vez no índice {}
      E aparece 'A' pela última vez no índice {}
'''.format(frase.title() , frase.count("A"), (str.find(frase, "A")) + 1, (str.rfind(frase, "A"))))
qlqr = input('Escreva uma frase qualquer: ')
print('''
      A frase "{}" tem {} letra(s) a(s)
      A letra 'A' aparece a primeira vez no índice {}
'''.format(qlqr, qlqr.count('a'), (str.find(qlqr, "a")) + 1))
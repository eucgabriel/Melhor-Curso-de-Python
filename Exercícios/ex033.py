num1 = int(input('Indique o 1º nº:'))
num2 = int(input('Indique o 2º nº:'))
num3 = int(input('Indique o 3º nº:'))

num = [num1, num2, num3]
print('''
      "{}" é o maior nº
      "{}" é o menor nº
      '''.format(max(num), min(num))) 
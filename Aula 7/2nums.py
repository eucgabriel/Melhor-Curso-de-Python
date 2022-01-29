n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('''
      A soma vale {}
      A subtração vale {}
      A multiplicação vale {}
      A divisão vale {}
      A potência vale {}
      A divisão inteira vale {}
      O módulo vale {}
'''.format(n1+n2, n1-n2, n1*n2, n1/n2, n1**n2, n1//n2, n1 % n2))

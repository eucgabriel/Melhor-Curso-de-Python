sal = float(input('Qual seu salário?'))
if(sal < 1250):
    aum = sal + ((15/100)*sal)
    print('''
          O seu salário era R${:,.2f}
          Com o aumento de 15% virou R${:,.2f}
          '''.format(sal, aum))
else:
    aum = sal + ((10/100)*sal)
    print('''
          O seu salário era R${:,.2f}
          Com o aumento de 10% virou R${:,.2f}
          '''.format(sal, aum))
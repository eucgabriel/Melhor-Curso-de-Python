num = int(input('Diga um nº de 1 a 9999:'))
n = str(num)
if(num < 10) and (num > 0):
    mil = 0
    cent = 0
    dez = 0
    print('''
          MILHAR   CENTENA    DEZENA    UNIDADE
            {}        {}        {}        {}
    '''.format(mil, cent, dez, n[0]))
elif(num >= 10) and (num < 100) and (num > 0):
    mil = 0
    cent = 0
    print('''
          MILHAR   CENTENA    DEZENA    UNIDADE
            {}        {}        {}        {}
    '''.format(mil, cent, n[0], n[1]))
elif(num >= 100) and (num < 1000) and (num > 0):
    mil = 0
    print('''
          MILHAR   CENTENA    DEZENA    UNIDADE
            {}        {}        {}        {}
    '''.format(mil, n[0], n[1], n[2]))
elif(num < 10000) and (num >= 1000) and (num > 0):
    print('''
          MILHAR   CENTENA    DEZENA    UNIDADE
            {}        {}        {}        {}
    '''.format(n[0], n[1], n[2], n[3]))
elif(num < 0):
    print('Esse nº é menor que 0')
else:
    print('Esse nº é maior do que o pedido')

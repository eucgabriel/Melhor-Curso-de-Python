v = float(input('Indique quanto ta a temperatura ai(em Celsius):'))
print('='*43)
print('''
    A temperatura indicada foi de {:.1f}ºC
    Corresponde à                 {:.1f}ºF
'''.format(v, v*1.8 + 32))
print('='*43)

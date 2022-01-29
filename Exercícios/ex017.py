from math import sqrt
co = float(input('Qual o Cateto Oposto do Triângulo?'))
ca = float(input('Agora qual o Cateto Adjacente dele:'))
print('''
        O Cateto Oposto é    {}
        O Cateto Adjacente é {}
        Agora a Hipotenusa é {:.2f}
'''.format(co, ca, sqrt((co**2)+(ca**2))))

import math
ang = float(input('Digite o ângulo dessa forma forma geométrica:'))
print('''
        O ângulo indicado é {}
        Seu seno é          {:.2f}
        Seu cosseno é       {:.2f}
        E sua tangente é    {:.2f}
'''.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))

nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))
print('''
        Nota do 1º Bimestre {:.1f}
        Nota do 2º Bimestre {:.1f}
        Média Final         {:.1f}
'''.format(nota1, nota2, (nota1+nota2)/2))

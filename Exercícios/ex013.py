s = float(input('Qual o valor do seu salário hoje?'))
print('''
        O seu salário era          R$ {:.2f}
        Com o aumento de 15% ta a  R$ {:.2f}
'''.format(s, s+(s*0.15)))

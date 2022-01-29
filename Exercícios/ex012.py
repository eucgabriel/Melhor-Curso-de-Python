v = float(input('Qual o valor do produto que deseja?'))
print('''
        O valor do produto é de R$ {:.2f}
        Na liquidação fica a    R$ {:.2f}
        
'''.format(v, v-(v*0.05)))

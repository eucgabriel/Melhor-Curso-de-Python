carteira = float(input('Quantos reais você tem na carteira?'))
cotacao = float(input('Qual a cotação do dólar nesse exato momento?'))
print('''
        Você tem R$ {:.2f}
        O que é  U$ {:.2f}
'''.format(carteira, carteira/cotacao))

m = float(input('''
        Digite qual o valor que você quer tranformar
        de metro pra centímetro e pra milímetro: 
'''))
print('''
        O valor em digitado é {:.0f}
        Ele em centímetros é {:.0f}cm
        Ele em milímetros é {:.0f}mm
'''.format(m, m*100, m*1000))

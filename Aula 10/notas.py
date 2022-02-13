n1 = float(input('Qual foi a tua 1ª nota?'))
n2 = float(input('Qual foi a tua 2ª nota?'))
m = (n1 + n2) / 2
print('''
        Sua média foi {:.1f}
'''.format(m))
if(m >= 7):
    print('Não fez mais do que a sua obrigação!!')
elif(m < 7) and (m > 4):
    print('Você está de recuperação!!!')
elif(m < 4):
    print('Parabéns, você é tão burro que reprovou!')
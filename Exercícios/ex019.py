import random
r1 = input('Informe o Nome do 1º aluno:')
r2 = input('Informe o Nome do 2º aluno:')
r3 = input('Informe o Nome do 3º aluno:')
r4 = input('E por fim o Nome do último aluno:')

list = [r1, r2, r3, r4]

result = random.choice(list)

print('O aluno sorteado para apagar o quadro foi {}!!!'.format(result))

frase = 'Curso em Vídeo Python'
print(frase.upper())  # Tudo Maiúsculo
print(frase.lower())  # Tudo Minúsculo
print(frase.capitalize())  # Só o 1º Maiúsculo
print(frase.title())  # Todo início de Palavra Maiúsculo
print(frase)

frase = '   Aprenda Python  '
print(frase.strip())  # Apaga dos os Espaços sem sentido
print(frase.rstrip())  # Direita
print(frase.lstrip())  # Esquerda

frase = 'Curso em Vídeo Python'
frase = frase.split()
print(''.join(frase))

##Recebimento de variáveis
nome = input("Qual seu nome?")
sexo = int(input('Qual seu sexo(Digite "1" para masculino e "2" para feminino)?'))
##if
if sexo == 1:
    result = f"""
          Olá Srº {nome}, seja bem vindo ao nosso programa,
          nós da CG Enterprise desejamos que com a gente
          tudo possa ser possível!!
          """
    print(result)
elif sexo == 2:
    result = f"""
          Olá Srª {nome}, seja bem vinda ao nosso programa!
          nós da CG Enterprise desejamos que com a gente
          tudo possa ser possível!!
          """
    print(result)

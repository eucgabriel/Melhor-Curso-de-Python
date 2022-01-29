x = input("Digite algo:")
print(
    """
      [01]Essa variável é alfanumérica? {}
      [02]Essa variável é alfabética? {}
      [03]Essa variável faz parte da ASCII? {}
      [04]Essa variável é decimal? {}
      [05]Essa variável é um nº de 0 a 9? {}
      [06]Essa variável é um identificador que pode ser
      usado como função, classes ou variáveis? {} 
      [07]Essa variável está com todos os caracteres
      minúsculos? {}
      [08]Essa variável é um valor númerico? {}
      [09]Essa variável é um valor imprimível? {}
      [10]Essa variável é um espaço em branco? {}
      [11]Essa variável é maiúscula? {}
      [12]Essa variável é totalmente maiúscula? {}
      """.format(
        x.isalnum(),
        x.isalpha(),
        x.isascii(),
        x.isdecimal(),
        x.isdigit(),
        x.isidentifier(),
        x.islower(),
        x.isnumeric(),
        x.isprintable(),
        x.isspace(),
        x.istitle(),
        x.isupper(),
    )
)

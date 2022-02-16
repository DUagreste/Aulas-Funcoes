"""# Argumentos nomeados

def imprimir_nome(nome, sobrenome, idade):  # parâmetro
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)

imprimir_nome(idade="25", nome="Vitor", sobrenome="Pinheiro")  # argumento"""

"""# Parâmetro padrão
def imprimir_nome(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print("nome:", nome)
        print("sobrenome:", sobrenome)
        print("idade:", idade)
        print(15*"-")
    else:
        print("Por favor, insira seus dados.")
        print(15*"-")

imprimir_nome()
imprimir_nome("Vitor", "Pinheiro", 25)

def imprimir_movel(nomeImovel, nQuartos, vagasGaragem=None):
    print("----------------------")
    print("Título:", nomeImovel)
    print("Quartos:", nQuartos)
    if vagasGaragem != None:
        print("Vagas na garagem:", vagasGaragem)

print()
# Exemplos de Nº ARGUMENTOS <= Nº PARÂMETROS
imprimir_movel("Kitnet - RN", 2)
imprimir_movel("Apartamento 2 suítes - SP", 3, 2)

# Exemplos de Nº ARGUMENTOS > Nº PARÂMETROS (vai dar erro)
imprimir_movel("Casa mobiliada - CE", 5, 3, 2)"""

# Argumento arbitrário (*args)

def imprimir_movel(nomeImovel, nQuartos, vagasGaragem=None, *nBanheiros):
    print("----------------------")
    print("Título:", nomeImovel)
    print("Quartos:", nQuartos)
    if vagasGaragem != None:
        print("Vagas na garagem:", vagasGaragem)
    print("Banheiros:", *nBanheiros)


imprimir_movel("Casa mobiliada - CE", 5, 3, 2)


"""def imprimir_nomes(*nomes):
    print(nomes)


lista = ["ana", "pedro", "joão", "vitor"]
imprimir_nomes(*lista)"""

""" Argumentos nomeados

def imprimir_nome(nome, sobrenome, idade):  # parâmetro
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)


imprimir_nome(idade="25", nome="Vitor", sobrenome="Pinheiro")  # argumento"""

# Parâmetro padrão


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

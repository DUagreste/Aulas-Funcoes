""" Argumentos nomeados

def imprimir_nome(nome, sobrenome, idade):  # parâmetro
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)


imprimir_nome(idade="25", nome="Vitor", sobrenome="Pinheiro")  # argumento"""

# Parâmetro padrão


def imprimir_nome(nome=None, sobrenome=None, idade=None):
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)


imprimir_nome()

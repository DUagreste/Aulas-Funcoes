# Funções - paradigma imperativo
# Variáveis, atribuições e sequência

# bloco externo
nome = "Gabriel"    # variável global


def minha_funcao():  # bloco interno *corpo da função logo abaixo
    nome = "Ana"    # variável local
    tupla = 2, 5, 6, 7, 8
    print(nome)
    print(tupla)
    for x in tupla:
        print(x)


minha_funcao()
print(nome)

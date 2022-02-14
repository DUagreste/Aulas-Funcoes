# Funções - paradigma imperativo
# Variáveis, atribuições e sequência

"""def ola_mundo():
    return "Olá, mundo"


retorno = ola_mundo()
print(retorno)

def minha_funcao():
    var = "Maria"
    return var  # O var de Maria não é definido fora da função


print(minha_funcao())
var = "Ana"
print(var)
"""


def imprimir_nome(nome):  # parâmetro: valores utilizados para definir
    # corpo da função
    print("Olá,", nome)


nome = input("Qual seu nome? ")
imprimir_nome(nome)    # argumento: valores de chamada da função

"""Não pode-se passar argumentos a menos ou a mais do que o estabelecido"""

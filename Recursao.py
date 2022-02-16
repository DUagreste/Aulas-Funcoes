"""def reduzirN(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirN(10)"""

"""
1 - checar se o nosso número não é 0
2 - caso não, reduzir 1

5 - 1 = 4
4 - 1 = 3
3 - 1 = 2
2 - 1 = 1
1 - 1 = 0

print(10*"-")


def reduzirNumber(nInt):
    print(nInt)
    if nInt > 0:
        # N - 1
        reduzirNumber(nInt - 1)


reduzirNumber(5)
"""
# Fatorial sem Recursão
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1,):
            fatorial *= x
        return fatorial


print(fatorialS(5))
print(5*"-")
# Fatorial com Recursão
def fatorialR(numero):
    if numero == 0: # Critério de paradaa
        return 1
    else:
        # Parâmetro recursivo
        return numero * fatorialR(numero - 1)


print(fatorialR(5))

def par_impar():
    numero = int(input("Digite um número: "))
    if (numero % 2) == 0:
        return "número par"
    return "número impar"

print(par_impar())

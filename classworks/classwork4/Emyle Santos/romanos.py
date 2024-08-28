def romanos(letras):
    lista_letras = list(letras)
    lista_letras.reverse()

    hash = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    soma = 0
    for i in range(len(lista_letras)):
        atual = hash[lista_letras[i]]
        
        if i == 0 or atual >= hash[lista_letras[i - 1]]:
            soma += atual
        else:
            soma -= atual

    return soma

letras = "DCCCXLV"
print(romanos(letras))  
# Initial Version

def two_sum(lista, k):
    somados = []

    for i in range(len(lista)-1):
        for j in range(len(lista)):
            if lista[i] + lista[j] == k and i != j and [lista[i], lista[j]] not in somados and [lista[j], lista[i]] not in somados:
                somados.append([lista[i], lista[j]])
    if somados == []:
        return False
    return True, somados
        
print(two_sum([1, 2, 3, 4], 5))

# Better Version

def two_sum(lista, k):
    somados = []

    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k and [lista[i], lista[j]] not in somados and [lista[j], lista[i]] not in somados:
                somados.append([lista[i], lista[j]])
    
    if not somados:
        return False
    
    return True, *somados # Desembrulhar a lista com *
        
print(two_sum([1, 2, 3, 4], 5))

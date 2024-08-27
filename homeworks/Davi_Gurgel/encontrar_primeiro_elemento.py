def repetido(lista):
    lvazia = []

    for i in lista:
        if i in lvazia:
            return i
        if i not in lvazia:
            lvazia.append(i)
        
    return False
    

def maior_numero_doces(doces, docesextras):
    
    maior = max(doces)

    lista= []

    for i in doces:
        if (i + docesextras) >= maior:
            lista.append(True)
        else: 
            lista.append(False)
    
    return lista 



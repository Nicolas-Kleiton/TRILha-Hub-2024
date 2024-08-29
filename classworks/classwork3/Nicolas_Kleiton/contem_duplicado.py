def duplicado (arr):

    # Um dicionário vazio para armazenar cada valor do arr
    dict = {}

    # Para cada elemento dentro do array, se ele não estiver no dict irá adiciona-lo ao dict.
    # Caso já esteja, significa que contém um duplicado, então retornará um False.
    for i in arr:
        if dict.get(i) is None:
            dict[i] = True
        else:
            return False
    
    # Depois de verificar cada elemento e não houver um duplicado, retornará True.
    return True
        
arr = [1,2,3,3,4,5,6]

print(duplicado(arr))
def duplicated(lista):
    return len(set(lista)) != len(lista)

print(duplicated([1,2,3,4,5,5,6,7]))

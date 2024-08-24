# First Version - O(n^2)
def repetido(lista):
    if len(set(lista)) == len(lista):
        return False
    
    aux = []
    for v in lista:
        if v not in aux:
            aux.append(v)
        else:
            return v

print(repetido([2,1,3,4,5,2,6]))

# Better Version - O(n)

def repetidos(lista):
    if len(set(lista)) == len(lista):
        return False
    
    hash = {}
    for v in lista:
        # if hash.get(v) is None:
        if v not in hash:
            hash[v] = v
        else:
            return v

print(repetidos([2,1,3,4,5,2,6]))

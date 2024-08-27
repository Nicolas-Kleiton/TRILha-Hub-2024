def romanos(number):
    sum = 0
    n = {'I' : 1,
         'V' : 5,
         'X' : 10,
         'L' : 50,
         'C' : 100,
         'D' : 500,
         'M' : 1000}
    
    lista = list(number)
    lista.reverse()
    
    for i in range(len(lista)):
        if i == 0 or n[lista[i]] >= n[lista[i-1]]:
            sum += n[lista[i]]
        else:
            sum -= n[lista[i]]
    
    return sum 

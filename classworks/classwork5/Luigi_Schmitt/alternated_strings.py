def mergeAlternately(word1, word2):
    if word1 == '':
        return word2
    if word2 == '':
        return word1
    
    list1 = list(word1)
    list2 = list(word2)
    list3 = []

    while True:
        try:
            list3.append(list1.pop(0))
            list3.append(list2.pop(0))
        except IndexError:
            break

    if list1 != '':
        for elemento in list1:
            list3.append(elemento)
    if list2 != '':
        for elemento in list2:
            list3.append(elemento)

    return ''.join(list3)

print(mergeAlternately("abc","pqr")) # deve retornar "apbqcr"
print(mergeAlternately("ab","pqrs")) # deve retornar "apbqrs"
print(mergeAlternately("","xyz")) # deve retornar "xyz"
print(mergeAlternately("a!b","@c#")) # deve retornar "a@!cb#"
print(mergeAlternately("abcd","pq")) # deve retornar "apbqcd"

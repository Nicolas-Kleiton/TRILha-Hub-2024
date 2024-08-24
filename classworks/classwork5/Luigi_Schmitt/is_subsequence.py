def isSubsequence(s, t):
    if s == '' or t == '':
        return True

    s = list(s)
    t = list(t)

    lista = []

    for i in range(len(t)):
        if t[i] in s:
            lista.append(t[i])

    return lista == s

print(isSubsequence('abc', 'ahbgdc')) # deve retornar True
print(isSubsequence('axc', 'ahbgdc')) # deve retornar False
print(isSubsequence('', 'ahbgdc')) # deve retornar True


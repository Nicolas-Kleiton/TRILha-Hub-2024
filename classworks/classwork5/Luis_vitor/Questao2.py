def isSubsequence(s, t):
    cont = 0
    if len(s) == 0:
        return True

    for letra in t:
        if letra == s[cont]:
            cont += 1
    
    if cont == len(s):
        return True

    return False
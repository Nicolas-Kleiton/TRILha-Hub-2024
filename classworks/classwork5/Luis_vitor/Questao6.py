def mergeAlternately(word1, word2):
    tam1 = len(word1)
    tam2 = len(word2)

    resp = ""

    if tam1 == tam2:
        for i in range(tam1):
            resp += word1[i]
            resp += word2[i]
    elif tam1 < tam2:
        for j in range(tam1):
            resp += word1[j]
            resp += word2[j]
        
        resp += word2[tam1::]
    else:
        for k in range(tam2):
            resp += word1[k]
            resp += word2[k]

        resp += word1[tam2::]
    
    return resp
        



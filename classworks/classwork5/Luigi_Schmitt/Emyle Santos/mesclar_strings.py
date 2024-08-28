def mergeAlternately(word1, word2):
    if word1 == "":
      return word2

    if word2 == "":
      return word1

    wordSum = []

    listaw1 = list(word1)
    listaw2 = list(word2)

    i = 0
    tammin = min(len(listaw1), len(listaw2))

    while  i < tammin:
       wordSum.append(listaw1[i])
       wordSum.append(listaw2[i])

       i += 1

    if len(listaw1) > tammin:
      wordSum += listaw1[tammin:]

    if len(listaw2) > tammin:
      wordSum += listaw2[tammin:]

    return ''.join(wordSum)

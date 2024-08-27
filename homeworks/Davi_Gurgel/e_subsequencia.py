def isSubsequence(s, t):
    x = list(t)
    y = list(s)
    lvazia = []
    for l in x:
      if l in y:
        lvazia.append(l)
    return lvazia == y
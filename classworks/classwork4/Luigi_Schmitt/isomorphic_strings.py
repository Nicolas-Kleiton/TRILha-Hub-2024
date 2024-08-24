def isomorphics(s, t):
    hashmap = {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if hashmap.get(s[i]) == None:
            for k in hashmap:
                if hashmap[k] == t[i]:
                    return False
            hashmap[s[i]] = t[i]
        else: 
            if hashmap[s[i]] != t[i]:
                return False

    return True
    
p1 = "badc"
p2 = "baba"

print(isomorphics(p1, p2))

# First Version
def romans(s):
    hash = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0
    prev = 0
    for i in range(len(s)-1, -1, -1):
        curr = hash[s[i]]
        if curr < prev:
            sum -= curr
        else:
            sum += curr
        prev = curr

    return sum

print(romans("MCMXCIV"))


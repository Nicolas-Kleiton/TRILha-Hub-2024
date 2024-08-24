def findDifference(nums1, nums2):
    resposta1 = []
    resposta2 = []

    for n in set(nums1):
        if n not in nums2:
            resposta1.append(n)

    for x in set(nums2):
        if x not in nums1:
            resposta2.append(x)

    return [resposta1, resposta2]

print(findDifference([1, 2, 3], [2, 4, 6])) # deve retornar [[1,3],[4, 6]]
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # deve retornar [[3],[]]
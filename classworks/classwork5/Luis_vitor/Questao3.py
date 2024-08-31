def findDifference(nums1, nums2):
    numeros1 = set(nums1)
    numeros2 = set(nums2)

    intersection = numeros1.intersection(numeros2)

    lista = [list(numeros1 - intersection), list(numeros2 - intersection)]
    return lista

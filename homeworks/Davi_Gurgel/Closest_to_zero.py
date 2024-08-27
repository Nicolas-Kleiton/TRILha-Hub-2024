def findClosestNumber(nums):
    prox = nums[0]
    if prox == 0:
        return prox

    for i in range(len(nums)):
        if abs(nums[i]) < abs(prox):
          prox = nums[i]
        elif abs(nums[i]) == abs(prox) and nums[i] > prox:
          prox = nums[i]

    return prox
def findClosestNumber(nums):
    closest = 10000
    for num in nums:
        if abs(num) <= abs(closest):
            closest = num

    return closest

print(findClosestNumber([-4,-2,1,4,8])) # deve retornar 1
print(findClosestNumber([2,-1,1])) # deve retornar 1
print(findClosestNumber([0, 5, 10, -3, 7])) # deve retornar 0
print(findClosestNumber([-10, -5, -8, -1, -7])) # deve retornar -1
print(findClosestNumber([-3, 3, 5, -5])) # deve retornar 3

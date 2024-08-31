def findClosestNumber(nums):
    # remova o pass e escreva o codigo aqui
    resp = nums[0]
    print(resp)
    for n in nums[1::]:
        if abs(n) < abs(resp):
            resp = n
        elif abs(n) == abs(resp):
            if n > resp:
                resp = n
    return resp




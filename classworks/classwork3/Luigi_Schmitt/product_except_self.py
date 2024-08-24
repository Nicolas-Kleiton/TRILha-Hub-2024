# First Version - O(n^2)

def productExceptSelf(nums):
    resposta= []
    product = 1
    for i in range(len(nums)):
        l = i
        r = i

        while l > 0:
            l -= 1
            product *= nums[l]
        while r < len(nums)-1:
            r += 1
            product *= nums[r]

        resposta.append(product)
        product = 1
    
    return resposta

print(productExceptSelf(nums=[1,2,3,4]))
print(productExceptSelf(nums=[-1,1,0,-3,3]))

# Better Version - O(n)

def productExceptSelf2(nums):
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n

    for i in range(n):
        j = -i - 1   # Genial, vai interando como um Left e Right
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l*r for l,r in zip(l_arr, r_arr)] # zip para interar as duas ao mesmo tempo

print(productExceptSelf2(nums=[1,2,3,4]))
print(productExceptSelf2(nums=[-1,1,0,-3,3]))

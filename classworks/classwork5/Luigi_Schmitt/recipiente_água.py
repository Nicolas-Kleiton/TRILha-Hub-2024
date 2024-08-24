def maxArea(height):
    l = 0
    r = len(height)-1

    area_max = 0
    while l < r:
        area = (r-l) * min(height[l], height[r])
        if area > area_max:
            area_max = area
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return area_max

print(maxArea([1,8,6,2,5,4,8,3,7])) # deve retornar 49
print(maxArea([1,1])) # deve retornar 1
print(maxArea([4, 4, 4, 4])) # deve retornar 12
print(maxArea([5, 4, 3, 2, 1])) # deve retornar 6
print(maxArea([1, 3, 2, 5, 25, 24, 5])) # deve retornar 24

def maxArea(height):
    if height[0] < height[1]:
        area = height[0]
    else:
       area = height[1]

    for x in range(len(height)):
        count = 0
        for y in range (x + 1, len(height)):
            count += 1
            if min(height[x], height[y]) * count > area:
              area = min(height[x], height[y]) * count

    return area
def maxArea(height):
    esquerda = 0
    direita = len(height) - 1
    maior_area = 0

    while(esquerda != direita):
        area = min(height[esquerda], height[direita]) * (direita - esquerda)
            
        maior_area = max(area, maior_area)

        if height[direita] >= height[esquerda]:
            esquerda += 1
            
        else:
            direita -= 1

    return maior_area


print(maxArea([1, 3, 2, 5, 25, 24, 5]))
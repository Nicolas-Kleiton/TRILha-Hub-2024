# Can place flowers

def canPlaceFlowers(flowerbed, n) -> bool:
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1

    return n <= 0 # Se conseguirmos plantar todas as flores que queríamos

print(canPlaceFlowers([1,0,0,0,1], 1))

def produtoExcetoEle(nums):
    n = len(nums)
    resposta = [1] * n
    
    # Calculando prefixos
    prefixo = 1
    for i in range(n):
        resposta[i] = prefixo
        prefixo *= nums[i]
    
    # Calculando sufixos e multiplicando diretamente
    sufixo = 1
    for i in range(n - 1, -1, -1):
        resposta[i] *= sufixo
        sufixo *= nums[i]
    
    return resposta
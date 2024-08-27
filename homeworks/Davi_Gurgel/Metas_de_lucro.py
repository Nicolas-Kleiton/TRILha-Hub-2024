def stockPairs(stocksProfit, target):
    vazio = set()

    for x in range(len(stocksProfit)):
        for y in range (x + 1, len(stocksProfit)):
            if stocksProfit[x] + stocksProfit[y] == target:
                vazio.add(tuple(sorted((stocksProfit[x], stocksProfit[y]))))

    return len(vazio)
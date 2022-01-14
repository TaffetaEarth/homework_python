def rec(dict, combin, result):
    if len(combin == 0):
        return result
    k = 0
    while k < len(result):
        for i in range(3 ** len(combin)):
            result[k] += dict[combin[0]][0]
            k += 1
        for i in range(3 ** len(combin)):
            result[k] += dict[combin[0]][1]
            k += 1
        for i in range(3 ** len(combin)):
            result[k] += dict[combin[0]][2]
            k += 1
    combin = combin.pop(0)
    rec(dict, combin, result)

# 1435
# abcd

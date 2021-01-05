def reverse(candles):
    count = 0
    tall = candles[0]
    for i in range(len(candles)-1):
        if tall>candles[i]:
            pass
        elif tall<candles[i]:
            tall = candles[i]
    for j in range(len(candles)):
        if candles[j] == tall:
            count += 1
        j+=1

    return count
lol = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]
print(reverse(lol))





    


from collections import OrderedDict 
def divisibleSumPairs(n, k, ar):
    res = []
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i]+ar[j])%k == 0:
                res.append([ar[i], ar[j]])
            else: 
                continue
    
    return len(res)
arr = [1, 3, 2, 6, 1, 2]
k = 3

print(divisibleSumPairs(6, k, arr))

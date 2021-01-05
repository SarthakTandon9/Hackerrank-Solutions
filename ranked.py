
def nonDivisibleSubset(k, s):
    f = [0]*k
    for i in s:
        f[i%k] += 1
    result = 0
    for a in range(0, (k+1)/2):
        result += max(f[a], f[k-a])
    if k % 2 == 0 and f[k/2]:
        result += 1
    if f[0]:
        result += 1
    return result



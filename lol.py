from collections import Counter
def nonDivisibleSubset(a):
    c = Counter((i%k for i in a))
    count = 0
    blacklist = set()
    for x,y in c.most_common():
        if x == k/2 or x==0:
            count+=1
        elif k-x not in blacklist:
            count+=y
            blacklist.add(x)
    return count

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(nonDivisibleSubset(a))
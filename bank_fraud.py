import statistics
def activityNotifications(expenditure, d):
    n = d
    data = []
    notify = 0
    med = 0
    lis = [1, 1]
    for i in range(len(expenditure)):
        if n+1<len(expenditure):
            data = []
            data = expenditure[:n]
            data = sort(data)
            med = int(median(data))
            print(med, data)
            if med >= 2*(expenditure[n+1]):
                notify += 1
                n += 1
            else: 
                n +=1
                continue
        else:
            break
        
    return notify

def sort(a):
    print(sorted(a))
    return sorted(a)
def median(arr):
    median = statistics.median(arr)
    return median

n = 5
data = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(int(3.5))

    
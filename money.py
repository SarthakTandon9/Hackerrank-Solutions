def getMoneySpent(keyboards, drives, budget):
    keyboards = sorting(keyboards)
    drives = sorting(drives)
    retVal = []
    
    for i in keyboards:
        for j in drives:
            if i+j < budget:
                retVal.append(i+j)
    return max(retVal)


def sorting(arr):
    return sorted(arr)
    


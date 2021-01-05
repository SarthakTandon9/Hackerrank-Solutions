def surfaceArea(A):
    retVal = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            retVal = (retVal + (A[i][j]*6)) - (A[i][j] - 1)
    return retVal

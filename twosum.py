#Getting target and num from the user. 
num = [int(item) for item in input("Enter the list items : ").split()] 
target = int(input("Please enter the target: "))
ans = []

#Creating a function to compute the result. 
def retValue(num, target):

    for i in range(len(num)):
        for j in range(len(num)-1):
            j += 1
            if (num[i] + num[j] == target):
                if(i == j):
                    pass
                else:
                    return i, j
            else: 
                pass
            
        i += 1
    
# calling the function and printing the value.         
ans = retValue(num, target) 
print(ans)
import math

def encryption(S):
    ls = []
    retVal = ""
    S = S.replace(" ", "")
    columns = math.ceil(math.sqrt(len(S)))
    rows = columns-1
    print(rows, columns)
    if rows*columns <len(S):
        rows+=1
    i = 0
    arr = []
    for r in range(rows):
        temp_list = []
        for j in range(columns):
            if i<len(S):
                temp_list.append(S[i])
                i += 1
            else:
                temp_list.append("")
        arr.append(temp_list)
    res = []
    for k in range(columns):
        temp_list = []
        for l in range(rows):
            temp_list.append(arr[l][k])
        res.append(''.join(temp_list))
        print(res)
    return (' '.join(res))
            

            






message = "chillout"
print(encryption(message))

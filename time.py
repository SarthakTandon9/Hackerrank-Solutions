def timeInWords(h, f):
    upper_val = 0
    if h == 12:
        upper_val = 1
    else:
        upper_val = (h+1)
    if f>30:
        if f==45:
            return 'quarter to ' + numToWord(upper_val)
        else:
            return numToWord((60-f)) + ' ' + 'minutes to ' + numToWord(upper_val)
    elif f == 30:
        return 'half past ' + numToWord(h)
    elif f<30 and f>0:
        if f==15:
            return 'quarter past ' + numToWord(h)                                                      
        elif f == 1:
            return 'one minute past ' + numToWord(h)
        else:
            return numToWord(f) + ' minutes past ' + numToWord(h)
    elif f == 0:
        return numToWord(h) + " o' clock"  

def numToWord(num):
    nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens_dict = {2:'twenty', 3:'thirty'}
    if num>30:
        num = 60-num
    if num>=1 and num<= 19:
        return nums[num]
    elif num>19:
        tens, ones = divmod(num, 10)
        retVal = tens_dict[tens] + ' ' + nums[ones]
        return retVal
    else:
        return 'error'
print(timeInWords(1, 1))
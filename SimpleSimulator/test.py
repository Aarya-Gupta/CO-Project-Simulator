def findTwoscomplement(str):
    n=len(str)
    i=n-1
    while(i>=0):
        if(str[i]=='1'):
            break
 
        i-=1
    if i==-1:
        return '1'+str
    k=i-1
    while(k >= 0):
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
 
        k -= 1
    return str
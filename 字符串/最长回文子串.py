def centerspread(str,left,right):
    lenght=len(str)
    i=left
    j=right
    while i>=0 and j<lenght:
        if str[i]==str[j]:
            i-=1
            j+=1
        else:
            break
    return str[i+1:j]

def longestrome(str):
    lenght=len(str)
    if lenght <2:
        return  str
    maxlen=1
    res=str[0]
    for i in range(lenght-1):
        odd=centerspread(str,i,i)
        even=centerspread(str,i,i+1)
        maxstr=odd if len(odd)>len(even) else even
        if len(maxstr)>maxlen:
            maxlen=len(maxstr)
            res=maxstr
    return res

l=longestrome("adaad")
print(l)

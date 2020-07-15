def max(n1,n2):
    if n1<n2:
        min=n1
    else:
        min=n2
    max=1
    for i in range(1,min+1):
        if n1%i==0 and n2%i==0:
            max=i
    print(max)
    return max

if __name__ == '__main__':
    max(999,444)




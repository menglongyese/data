from typing import List
from random import randint
def bubblesort(l:List):
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
        print("{}".format(i),end="")
        print(l)
    return l
if __name__ == '__main__':
    l=[]
    for _ in range(20):
        l.append(randint(0,100))
    print(bubblesort(l))

from typing import List
from random import randint
def selectionSort(l:List):
    if len(l)<=1:
        return l
    for i in range(len(l)-1):
        minindex=i
        for j in range(i+1,len(l)):
            if l[j]<l[minindex]:
                minindex=j
        l[i],l[minindex]=l[minindex],l[i]
        print("第{}轮排序结果:".format(i),end="")
        print(l)
    return l
if __name__ == '__main__':
    l=[]
    for _ in range(20):
        l.append(randint(0,100))
    print(selectionSort(l))
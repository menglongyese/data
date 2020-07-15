from typing import List
from random import randint
def bubblesort(l:List):
    if len(l)<2:
        return l
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        print("第{}轮排序的结果:".format(i), end="")
        print(l)
    return l
if __name__ == '__main__':
    l = []
    for _ in range(20):
        l.append(randint(0, 100))
    bubblesort(l)



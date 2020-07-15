from typing import List
from random import randint
def insertsort(l:List):
    if len(l)<2:
        return l
    for i in range(len(l)):
        tar=l[i]
        for j in range(i):
            if tar<=l[j]:
                l[j+1:i+1]=l[j:i]
                l[j]=tar
                break
        print("第{}轮循环:".format(i+1),end="")
        print(l)
    return l
if __name__ == '__main__':
    l=[]
    for _ in range(20):
        l.append(randint(0,100))
    print("结果:{}".format( insersort(l)))






from typing import List
from random import randint
def insertsort(l:List):
    if len(l)<2:
        return l
    for right in range(len(l)):
        tar=l[right]
        for left in range(right):
            if tar <=l[left]:
                l[left+1:right+1]=l[left:right]
                l[left]=tar
                break
        print("第{}轮循环:".format(right + 1), end="")
        print(l)
    return l
if __name__ == '__main__':
    l = []
    for _ in range(20):
        l.append(randint(0, 100))
    print("结果:{}".format(insertsort(l)))

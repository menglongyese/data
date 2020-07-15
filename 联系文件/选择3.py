from typing import  List
from random import randint
def selection(l:List):
    if len(l)<2:
        return l
    for i in range(len(l)):
        minindex = i
        for j in range(i+1,len(l)):
            if l[j]< l[minindex]:
                minindex=j
        l[minindex],l[i]=l[i],l[minindex]
        print("第{}轮循环:".format(i+1),end="")
        print(l)
    return l
if __name__ == '__main__':
    l=[]
    for _ in range(20):
        l.append(randint(0,100))
    print(selection(l))

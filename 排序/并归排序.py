from random import randint
from typing import List
def mergesort(l: List):
    if len(l) < 2:
        return l
    middle = len(l) // 2
    left, right = l[0:middle], l[middle:]
    return merge(mergesort(left), mergesort(right))

def merge(left: List, right: List):
    mlist = []
    while left and right:
        if left[0] >= right[0]:
            mlist.append(right.pop(0))
        else:
            mlist.append(left.pop(0))
    while left:
        mlist.append(left.pop(0))
    while right:
        mlist.append(right.pop(0))
    return mlist

def merge1(left: List, right: List):
    left_len = len(left)
    right_len = len(right)
    mlist = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] <= right_len[j]:
            mlist.append(left[i])
            i += 1
        else:
            mlist.append(right[j])
            j += 1
    mlist.extend(left[i:])
    mlist.extend(right[j:])
    return mlist


if __name__ == '__main__':
    l = []
    for _ in range(20):
        l.append(randint(0, 100))
    print(l)

    print(mergesort(l))

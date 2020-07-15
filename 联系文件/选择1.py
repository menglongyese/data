import random
from typing import *


def lll(lis: List):
    if len(lis) <= 1:
        return lis
    for i in range(1, len(lis)):
        for j in range(len(lis) - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
        print("{}轮结果:{}".format(i, lis))


def llll(lis):
    if len(lis) <= 1:
        return lis
    for i in range(len(lis) - 1):
        index = i
        for j in range(i + 1, len(lis)):
            if lis[index] > lis[j]:
                index = j
        lis[index], lis[i] = lis[i], lis[index]
        print("{}轮结果:{}".format(i, lis))

"""
14 编写一个函数来查找字符串数组中的最长公共前缀。
链接：https://leetcode-cn.com/problems/longest-common-prefix

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

# a = [1, 2, 3]
# b = [4, 5, 6]
# zipped = list(zip(a, b))
# print(zipped)
# for each in zipped:
#     print(each)
#
# for each in zip(*zipped):
#     print(each)

# strs = ["flower", "flow", "flight"]
# minLength = min([len(s) for s in strs])
# print(minLength)

from typing import List

def longestCommonPrefix(strs: List[str]):
    if len(strs) == 0 or "" in strs: #判断列表长度如果为零返回空
        return ""
    if len(strs) == 1: #判断列表长度如果为一返回列表
        return strs
    minLength = min([len(s) for s in strs])
    publicWord = []
    for i in range(minLength):
        for word in strs:
            publicWord.append(word[:i+1])
        if len(set(publicWord)) == 1:
            publicWord = []
        else:
            return strs[0][:i]

["flower", "flow", "flight"]
# 使用 zip 根据字符串下标合并成数组，
# 判断合并后数组里元素是否都相同
def longCommonPrefix(strs: List[str]):
    res = ''
    for each in zip(*strs):
        if len(set(each)) == 1:
            res += each[0]
        else:
            return res
    return res
#
#
if __name__ == '__main__':
    l = ["flower", "flow", "flight"]
    print(longCommonPrefix(l))
    print(longestCommonPrefix(l))
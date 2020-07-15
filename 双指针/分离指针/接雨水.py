from typing import List
# 暴力解法
def trap(height:List[int]):
    # 初始化一些结果变量数组长度
    ans=0
    size=len(height)
    # 外层循环遍历每个位置
    for i in range(size):
        left_max=0  # 记录每个位置对应左侧最大值
        rigth_max=0 # 记录每个位置对应右侧最大值
        for j in range(i,size): # 找到当前柱子右边最高的主子, 并记录
            rigth_max=max(height[j],rigth_max)
        for j in range(i,-1,-1):# 找到当前柱子左边最高的主子记录
            left_max=max(height[j],left_max)
        # 计算当前位置能存多少雨水,并累加到结果上
        ans =ans+min(left_max,rigth_max)-height[i]
    return  ans

def trap1(list2):
    left=0
    right=len(list2)-1
    left_max=0
    right_max=0
    res=0
    while left<=right:
        left_max=max(left_max,list2[left])
        right_max=max(right_max,list2[right])
        if left_max<right_max:
            res+=left_max-list2[left]
            left+=1
        elif left_max>=right_max:
            res+=right_max-list2[right]
            res+=right_max-list2[right]
            right-=1
    return res
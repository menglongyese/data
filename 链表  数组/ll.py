nums=[1,3,2,5,10,5,4,6]
target=7
for left in range(len(nums)):
    right = len(nums) - 1
    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            print(left,right)
            right -= 1
        else:
            right -= 1

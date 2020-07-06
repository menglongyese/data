

def remove(nums, val):

    fast = 0
    slow = -1
    while fast < len(nums):
        if nums[fast] == val:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return


l = [0, 1, 2, 4, 0, 6, 0, 7]
remove(l, 2)
print(l)

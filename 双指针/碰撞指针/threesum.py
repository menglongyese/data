from typing import List


def threesum(nums: List[int], tar) -> List:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i >= 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < tar:
                left += 1
            elif sum > tar:
                right -= 1
            else:
                res.append([i, left, right])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res


print(threesum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
l = [1, 2, 3]
l.append()

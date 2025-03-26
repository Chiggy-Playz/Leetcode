# https://leetcode.com/problems/two-sum/
# Two Sum


def twoSum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        tar = target - num
        if tar in num_to_index:
            return [num_to_index[tar], i]
        else:
            num_to_index[num] = i
    return []

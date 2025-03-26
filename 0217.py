# https://leetcode.com/problems/contains-duplicate/description/
# Contains duplicate


def containsDuplicate(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

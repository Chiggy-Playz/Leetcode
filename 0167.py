# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 167. Two Sum II - Input Array Is Sorted


def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < len(numbers):

        needed = target - numbers[l]

        while numbers[r] > needed:
            r -= 1

        if numbers[r] == needed:
            return [l + 1, r + 1]

        l += 1

    return []


print(twoSum([1, 2, 7, 11, 15], 9))

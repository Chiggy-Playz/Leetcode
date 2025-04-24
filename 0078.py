from common import DoubleListNode, ListNode, TreeNode, null
from utils import equal_lists_unordered, test, time_it


def subsets(nums: list[int]) -> list[list[int]]:

    res = []

    subset = []

    def func(i: int):

        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        func(i + 1)

        subset.pop()
        func(i + 1)

    func(0)
    return res


test([[], [1]], equal_lists_unordered, subsets, [1])
test([[], [1], [2], [1, 2]], equal_lists_unordered, subsets, [1, 2])
test([[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]], equal_lists_unordered, subsets, [1, 2, 3])

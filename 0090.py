from common import null, TreeNode, ListNode, DoubleListNode
from utils import equal_lists_unordered, time_it, test

def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    result = []
    subset = []
 
    nums.sort()

    def dfs(nums):
        if not nums:
            result.append(subset.copy())
            return

        # Either choose the current one for subset
        subset.append(nums[0])
        dfs(nums[1:])
        subset.pop()

        # Skip current and move on
        i = 0
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        
        dfs(nums[i+1:])

    dfs(nums)
    return result

test(
    [[],[1],[1,2],[1,2,2],[2],[2,2]],
    equal_lists_unordered,
    subsetsWithDup,
    [1,2,2]
)
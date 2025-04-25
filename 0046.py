from common import null, TreeNode, ListNode, DoubleListNode
from utils import time_it, test, equal_lists_unordered

def permute(nums: list[int]) -> list[list[int]]:
    
    result = []

    current = []
    def dfs(nums):
        if not nums: 
            result.append(current.copy())
            return

        for i, num in enumerate(nums):
            current.append(num)
            dfs(nums[:i] + nums[i+1:])
            current.pop()
    
    dfs(nums)
    return result

test(
    [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
    equal_lists_unordered,
    permute,
    [1,2,3]
)
from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    results = []
    path = []

    def dfs(i: int, k: int):
        if k < 0 or i >= len(candidates):
            return

        if k == 0:
            results.append(path.copy())
            return

    
        path.append(candidates[i])
        dfs(i, k - candidates[i])
        path.pop()
        dfs(i+1, k)
    
    dfs(0, target)
    return list(results)


test([[2, 2, 3], [7]], None, combinationSum, [2, 3, 6, 7], 7)

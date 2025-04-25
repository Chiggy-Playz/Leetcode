from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:

    result = []
    path = []

    candidates.sort()

    def dfs(i: int, k: int):
        if k == 0:
            result.append(path.copy())
            return

        if k < 0 or i >= len(candidates):
            return

        current = candidates[i]
        path.append(current)
        dfs(i + 1, k - current)
        path.pop()
        # find the next element which is different from current
        while i < len(candidates):
            if current != candidates[i]:
                break
            i += 1
        dfs(i, k)

    dfs(0, target)
    return result


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

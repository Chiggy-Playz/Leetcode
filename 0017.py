from common import DoubleListNode, ListNode, TreeNode, null
from utils import equal_lists_unordered, test, time_it


def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(s: list[str]):
        if len(s) == 1:
            return list(s[0])

        rest = dfs(s[1:])
        res = []
        for char in s[0]:
            res.extend([char + i for i in rest])

        return res

    return dfs([keyboard[digit] for digit in digits])


test(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], equal_lists_unordered, letterCombinations, "23")

from common import null, TreeNode, ListNode, DoubleListNode
from utils import time_it, test

def climbStairs(n: int) -> int:
    total = 0
    
    def dfs(n):
        nonlocal total

        if n < 0:
            return

        if n == 0:
            total += 1
            return
        
        dfs(n-1)
        dfs(n-2)
    
    dfs(n)
    return total

print(climbStairs(38))
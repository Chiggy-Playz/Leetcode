from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

root = TreeNode.generateTreeFromNums([5, 3, 6, 2, 4, null, null, 1])
lowestCommonAncestor(root, root.left.left.left, root.left.right)

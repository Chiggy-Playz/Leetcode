from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it


def goodNodes(root: TreeNode) -> int:

    good = 0

    def dfs(node, maxVal):
        nonlocal good

        if node.val >= maxVal:
            good += 1

        if node.left:
            dfs(node.left, max(node.val, maxVal))
        if node.right:
            dfs(node.right, max(node.val, maxVal))

    dfs(root, root.val)
    return good


test(
    4,
    None,
    goodNodes,
    TreeNode.generateTreeFromNums([3, 1, 4, 3, null, 1, 5]),
)

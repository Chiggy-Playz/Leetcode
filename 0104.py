from common import DoubleListNode, ListNode, TreeNode
from utils import test, time_it


def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


test(
    3,
    TreeNode.equals,
    maxDepth,
    TreeNode.generateTreeFromNums([3, 9, 20, None, None, 15, 7]),
)

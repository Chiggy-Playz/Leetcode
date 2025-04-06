from common import DoubleListNode, ListNode, TreeNode
from utils import test, time_it


def invertTree(root: TreeNode | None):
    if not root:
        return

    q = [root]
    while q:
        node = q.pop(0)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

        node.left, node.right = node.right, node.left

    return root


test(
    TreeNode.generateTreeFromNums([4, 7, 2, 9, 6, 3, 1]),
    TreeNode.equals,
    invertTree,
    TreeNode.generateTreeFromNums([4, 2, 7, 1, 3, 6, 9]),
)

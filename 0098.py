from common import DoubleListNode, ListNode, TreeNode, null
from utils import test, time_it


def isValidBST(root: TreeNode | None) -> bool:
    if not root:
        return True

    def dfs(node, maxVal=None, minVal=None):
        if not node:
            return True

        if maxVal is not None and node.val >= maxVal:
            return False

        if minVal is not None and node.val <= minVal:
            return False

        return dfs(node.left, node.val, minVal) and dfs(node.right, maxVal, node.val)

    return dfs(root.left, maxVal=root.val) and dfs(root.right, minVal=root.val)


test(True, None, isValidBST, TreeNode.generateTreeFromNums([2, 1, 3]))

test(False, None, isValidBST, TreeNode.generateTreeFromNums([5, 1, 4, null, null, 3, 6]))

test(False, None, isValidBST, TreeNode.generateTreeFromNums([5, 4, 6, null, null, 3, 7]))

test(False, None, isValidBST, TreeNode.generateTreeFromNums([0,null,-1]))

test(False, None, isValidBST, TreeNode.generateTreeFromNums([32,26,47,19,null,null,56,null,27]))
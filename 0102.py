from common import null, TreeNode, ListNode, DoubleListNode
from utils import time_it, test

def levelOrder(root: "TreeNode | None") -> list[list[int]]:
        if not root:
            return []
        
        res = []
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)

            if len(res) > level:
                res[level].append(node.val)
            else:
                res.append([node.val])

            if node.left:
                q.append((node.left,level+1))
            
            if node.right:
                q.append((node.right, level+1))
        
        return res

test(
     [[3],[9,20],[15,7]],
     None,
     levelOrder,
     TreeNode.generateTreeFromNums([3,9,20,null,null,15,7])
)
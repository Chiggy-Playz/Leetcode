# Definition for a binary tree node.
class TreeNode:
    """
    Class for treenode
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode ({self.val})"


def getTree1():
    r"""
    Returns a binary tree with the following structure:
    ```
                      1
                   /     \
                2          3
              /  \       /   \
            4      5    6     7
           / \    / \  / \   / \
         8    9 10 11 12 13 14 15
    ```
    """
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node12 = TreeNode(12)
    node13 = TreeNode(13)
    node14 = TreeNode(14)
    node15 = TreeNode(15)

    node4 = TreeNode(4, node8, node9)
    node5 = TreeNode(5, node10, node11)
    node6 = TreeNode(6, node12, node13)
    node7 = TreeNode(7, node14, node15)

    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, node6, node7)

    root = TreeNode(1, node2, node3)

    return root


def generateTree(nums: list[int | None]) -> TreeNode:
    """
    Generates a binary tree from a list of integers. Level order traversal.
    """

    if len(nums) == 0:
        raise ValueError("nums cannot be empty")

    nodes = [None if num is None else TreeNode(num) for num in nums]

    for i, node in enumerate(nodes):
        if node is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            node.left = nodes[left]

        if right < len(nodes):
            node.right = nodes[right]

    assert nodes[0] is not None
    return nodes[0]



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: "ListNode | None" = next
    
    def __repr__(self) -> str:
        return f"<Listnode value={self.val} next={self.next.val if self.next else None}>"

    def chain(self):
        return f"{self.val} -> {self.next.chain() if self.next else None}"

    @staticmethod
    def generate_from(l: list[int]):
        if not l:
            return
        
        head = ListNode(l[0])
        current = head
        for val in l[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head
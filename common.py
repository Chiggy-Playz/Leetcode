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

    @staticmethod
    def generateTree(nums: list[int | None]) -> "TreeNode":
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

    @staticmethod
    def generateFullTree(height: int = 4):
        return TreeNode.generateTree(list(range(1, 2**height)))

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

    @staticmethod
    def equals(l1: "ListNode | None", l2: "ListNode | None") -> bool:
        if not (isinstance(l1, ListNode) and isinstance(l2, ListNode)):
            return False

        return l1.chain() == l2.chain()


class DoubleListNode:
    def __init__(self, val=0, next: "DoubleListNode | None" = None, prev: "DoubleListNode | None" = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"<Listnode value={self.val} next={self.next.val if self.next else None} prev={self.prev.val if self.prev else None}>"

    def chain(self):
        return f"{self.val} <-> {self.next.chain() if self.next else None}"

    @staticmethod
    def generate_from(l: list[int]):
        if not l:
            return None
        
        head = DoubleListNode(l[0])
        current = head
        for value in l[1:]:
            new_node = DoubleListNode(value)
            current.next = new_node
            new_node.prev = current
            current = new_node
        
        return head
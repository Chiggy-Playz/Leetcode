null = None

# Definition for a binary tree node.
class TreeNode:
    """
    Class for treenode
    """

    def __init__(self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode ({self.val})"

    @staticmethod
    def generateTreeFromNums(nums: list[int | None]) -> "TreeNode":
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
    def generateTreeFromHeight(height: int = 4):
        return TreeNode.generateTreeFromNums(list(range(1, 2**height)))

    @staticmethod
    def equals(t1: object | None, t2: object | None):
        if not isinstance(t1, TreeNode) or not isinstance(t2, TreeNode):
            return t1 is t2

        if t1.val != t2.val:
            return False

        return TreeNode.equals(t1.left, t2.left) and TreeNode.equals(t1.right, t2.right)

    def display(self, prefix="", is_left=True):
        """
        Print the tree vertically with connector lines.
        """

        # Print the right subtree first (will appear at the top)
        if self.right:
            self.right.display(prefix + ("│   " if is_left else "    "), False)

        # Print the current node
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(self.val))

        # Print the left subtree (will appear at the bottom)
        if self.left:
            self.left.display(prefix + ("    " if is_left else "│   "), True)


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


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parents = list(range(size))
        self.size = [1] * size

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.size[rootY] > self.size[rootX]:
            self.parents[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]

        return True

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

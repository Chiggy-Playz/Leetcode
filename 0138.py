from common import ListNode


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        return f"<Listnode value={self.val} next={self.next.val if self.next else None} random={self.random.val if self.random else None}>"

    def chain(self):
        return f"{self.val} -> {self.next.chain() if self.next else None}"

    @staticmethod
    def generate_from(l: list[int]):
        head = Node(l[0])
        current = head
        for val in l[1:]:
            current.next = Node(val)
            current = current.next

        return head


def copyRandomList(head: "Node | None") -> "Node | None":

    if not head:
        return

    copies = {}
    dummy = Node(0)
    current = head
    while current:
        cloned = copies.get(current, Node(current.val))
        
        if current.next:
            next = copies.get(current.next, Node(current.next.val))
            copies[current.next] = next
            cloned.next = next

        if current.random:
            if current.random == current:
                cloned.random = cloned
            else:
                random = copies.get(current.random, Node(current.random.val))
                copies[current.random] = random
                cloned.random = random

        copies[current] = cloned
        current = current.next

    return copies[head]


head = Node.generate_from([7, 13, 11, 10, 1])

head.next.random = head  # 13 -> 7
head.next.next.random = head.next.next.next.next  # 11 -> 1
head.next.next.next.random = head.next.next  # 10 -> 11
head.next.next.next.next.random = head  # 1 -> 7

ans = copyRandomList(head)

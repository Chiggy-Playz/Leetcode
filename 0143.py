from math import ceil

from common import ListNode


def reorderList(head: ListNode | None) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    current = head
    tail = None
    parent = {}
    while current:
        parent[id(current.next)] = current
        if current.next is None:
            tail = current
        current = current.next

    dummy = ListNode()
    current = dummy

    if len(parent) == 1:
        return

    for _ in range(ceil(len(parent) / 2)):

        templ = head.next
        tempr = parent[id(tail)]

        head.next = None
        tail.next = None

        current.next = head
        if head == tail:
            break
        current.next.next = tail
        current = current.next.next

        head = templ
        tail = tempr

    return dummy.next


ans = reorderList(ListNode.generate_from([1]))
breakpoint()

from common import DoubleListNode, ListNode, TreeNode
from utils import test, time_it


def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    if not lists:
        return

    dummy = ListNode()
    current = dummy
    while lists:
        smallest = None
        si = 0
        i = 0

        while i < len(lists):
            node = lists[i]
            if not node:
                lists.pop(i)
                continue

            if smallest is None or node.val < smallest.val:
                smallest = node
                si = i

            i += 1

        if smallest is None:
            continue
        
        lists[si] = smallest.next

        current.next = smallest
        current = current.next
        current.next = None

    return dummy.next


test(
    ListNode.generate_from([1, 1, 2, 3, 4, 4, 5, 6]),
    ListNode.equals,
    mergeKLists,
    [
        ListNode.generate_from([1,4,5]),
        ListNode.generate_from([1,3,4]),
        ListNode.generate_from([2,6]),
    ],
)

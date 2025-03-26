from common import ListNode


def removeNthFromEnd(head: ListNode | None, k: int) -> ListNode | None:

    if not head:
        return

    i = 1
    current = head
    mapping = {}
    while current:
        mapping[i] = current
        current = current.next
        i += 1

    n = len(mapping)
    val = n - (k - 1)
    
    if val == 1:
        head = head.next
    else:
        mapping[val-1].next = mapping.get(val+1)

    return head

removeNthFromEnd(ListNode.generate_from([1]), 1)

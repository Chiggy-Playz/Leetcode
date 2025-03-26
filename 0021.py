from common import ListNode


def mergeTwoLists(i: ListNode | None, j: ListNode | None) -> ListNode | None:

    if not i or not j:
        return i or j

    dummy = ListNode()
    tail = dummy

    while i and j:

        if i.val <= j.val:
            tail.next = i
            i = i.next
        else:
            tail.next = j
            j = j.next
        
        tail = tail.next

    if i:
        tail.next = i

    if j:

        tail.next = j

    return dummy.next


a = ListNode.generate_from([1, 2, 4])
b = ListNode.generate_from([1, 3, 4])

ans = mergeTwoLists(a, b)
breakpoint()

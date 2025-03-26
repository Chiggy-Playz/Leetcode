
from common import ListNode
from utils import test


def reverseList(head: ListNode | None) -> ListNode | None:
    if not head:
        return
    
    current = head
    next = current.next

    if not next:
        return current
    current.next = None
    while next:
        temp = next.next
        next.next = current
        current, next = next, temp
    
    return current


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

ans = reverseList(one)
print(ans)
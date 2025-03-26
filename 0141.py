from common import ListNode
from utils import test

def hasCycle(self, head: ListNode | None) -> bool:
    if not head:
        return False
    
    slow = fast = head

    while fast:
        fast = fast.next
        if not fast or not slow:
            return False
        fast = fast.next
        slow = slow.next

        if fast == slow:
            return True
    
    return False

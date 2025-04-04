from common import ListNode


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

    carry = 0
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        current.next = ListNode((l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val + carry) // 10
        l1 = l1.next
        l2 = l2.next
        current = current.next
    
    while l1:
        current.next = ListNode((l1.val + carry) % 10)
        carry = (l1.val + carry) // 10
        l1 = l1.next
        current = current.next

    while l2:
        current.next = ListNode((l2.val + carry) % 10)
        carry = (l2.val + carry) // 10
        l2 = l2.next
        current = current.next
        
    if carry:
        current.next = ListNode(carry)

    return dummy.next       

a = ListNode.generate_from([9,9,9,9,9,9,9])
b = ListNode.generate_from([9,9,9,9])

print(addTwoNumbers(a, b))
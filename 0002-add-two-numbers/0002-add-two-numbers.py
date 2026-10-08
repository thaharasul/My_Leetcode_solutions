# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            def toInt(node):
                digits = []
                while node:
                    digits.append(str(node.val))
                    node = node.next
                return int(''.join(reversed(digits)))
            total = toInt(l1) + toInt(l2)
            digits = list(str(total))[::-1]
            dummy = ListNode(0)
            curr = dummy
            for d in digits:
                curr.next = ListNode(int(d))
                curr = curr.next
            return dummy.next
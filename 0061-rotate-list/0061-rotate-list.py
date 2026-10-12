# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
            if not head:
                return head
            vals = []
            node = head
            while node:
                vals.append(node.val)
                node = node.next
            n = len(vals)
            k %= n
            rotated = vals[-k:] + vals[:-k] if k else vals
            dummy = ListNode(0)
            curr = dummy
            for v in rotated:
                curr.next = ListNode(v)
                curr = curr.next
            return dummy.next
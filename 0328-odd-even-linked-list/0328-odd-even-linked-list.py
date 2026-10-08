# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
            odd, even = [], []
            node = head
            i = 1
            while node:
                (odd if i % 2 else even).append(node.val)
                node = node.next
                i += 1
            vals = odd + even
            node = head
            for v in vals:
                node.val = v
                node = node.next
            return head
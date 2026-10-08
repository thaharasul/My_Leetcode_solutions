# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        node = head
        for _ in range(count // 2):
            node = node.next
        return node
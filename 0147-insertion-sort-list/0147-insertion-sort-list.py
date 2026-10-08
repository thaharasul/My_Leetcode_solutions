# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
            values = []
            node = head
            while node:
                values.append(node.val)
                node = node.next
            values.sort()
            dummy = ListNode(0)
            curr = dummy
            for v in values:
                curr.next = ListNode(v)
                curr = curr.next
            return dummy.next
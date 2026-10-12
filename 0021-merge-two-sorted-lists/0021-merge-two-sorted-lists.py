# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
            vals = []
            for node in (list1, list2):
                while node:
                    vals.append(node.val)
                    node = node.next
            vals.sort()
            dummy = ListNode(0)
            curr = dummy
            for v in vals:
                curr.next = ListNode(v)
                curr = curr.next
            return dummy.next
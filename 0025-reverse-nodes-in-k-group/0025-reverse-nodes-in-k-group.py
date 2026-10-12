# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
            vals = []
            node = head
            while node:
                vals.append(node.val)
                node = node.next
            result = []
            for i in range(0, len(vals), k):
                chunk = vals[i:i + k]
                if len(chunk) == k:
                    chunk.reverse()
                result.extend(chunk)
            dummy = ListNode(0)
            curr = dummy
            for v in result:
                curr.next = ListNode(v)
                curr = curr.next
            return dummy.next